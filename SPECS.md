# Agrama V1 Developer Specification

**Implementation on local Valkey + Ollama up to an MCP-compatible server, with a test/benchmark-first workflow**

---

## 0 · Quick Recap

Agrama is a local micro-stack—**Valkey 8.1** for KV + graph, **Faiss 1.11** for vector search, **Ollama** running `qwen3:1.7b` for summarisation, all wrapped by a **FastAPI MCP server** and a **lazygit-style TUI** built with **Textual**.  You get sub-millisecond direct look-ups, < 50 ms semantic search, and a CLI one-liner—`docker compose up`—that works the same on macOS, Linux, and Windows 11 (now that Windows ships MCP support) ([GitHub][1], [GitHub][2], [GitHub][3], [The Verge][4]).

---

## 1 · Stack Versions & Why They Matter

| Layer      | Version                        | Highlights                                                                                                | Sources                |
| ---------- | ------------------------------ | --------------------------------------------------------------------------------------------------------- | ---------------------- |
| Valkey     | **8.1.1**                      | SIMD `BITCOUNT` path, TLS crash fix, CVE-2025-21605 patch, binary-compatible with Redis 7.2 ([GitHub][1]) | turn1view0             |
| Faiss      | **1.11.0**                     | `RaBitQ`, cosine metric, `IndexIDMap` w/ CAGRA, ARM OpenBLAS 0.3.29, overflow fixes ([GitHub][2])         | turn2view0             |
| Embeddings | `jina-embeddings-v3`           | 1024-d multilingual, 94 lang MTEB leader ([Hugging Face][5])                                              | turn5search0           |
| LLM        | `qwen3:1.7b` on Ollama ≥ 0.6.6 | 40 k ctx, MoE, 5 GB Q4\_K\_M bin ([Ollama][6])                                                            | turn12search0          |
| MCP        | spec v0.13                     | Open protocol repo + reference servers ([GitHub][7], [GitHub][8])                                         | turn6search0 / 1       |
| TUI        | Textual 0.52                   | Rich widgets + `Tree` & `DirectoryTree` ([GitHub][3], [Textual Documentation][9])                         | turn3view0 / 13search0 |

---

## 2 · Directory Layout

```
agrama/
├─ agrama/               # python package
│  ├─ api/               # FastAPI routers (AAP + MCP proxy)
│  ├─ db/                # Valkey client + graph helpers
│  ├─ vector/            # Faiss wrapper
│  ├─ proto/             # *.proto (compiled via buf)
│  ├─ summariser/        # Ollama client
│  └─ tests/
├─ tui/                  # Textual app
├─ docker/               # compose, Dockerfiles, healthchecks
├─ bench/                # pytest-benchmark json & compare script
└─ k6/                   # load tests
```

---

## 3 · Data Model & Key Schema (Valkey)

### 3.1 Node Encoding

```protobuf
message Node {
  string uuid = 1;
  string type = 2;          // Session | Task | CodeUnit …
  int64  created_at = 3;
  int64  updated_at = 4;
  bytes  content = 5;       // protobuf-packed struct or raw bytes
  repeated float embedding = 6 [packed=true];
}
```

* **Serialization:** `buf generate` → compact varint framing; ≈ 45 B/node for metadata.

### 3.2 Key Conventions

| Purpose   | Pattern                                     | TTL  |
| --------- | ------------------------------------------- | ---- |
| Node blob | `mem:{uuid}` → `<proto bytes>`              | ∞    |
| Out edges | `mem:{src}:out:{etype}` → `[dst1 … dstN]`   | ∞    |
| In edges  | `mem:{dst}:in:{etype}`  → `[src1 … srcN]`   | ∞    |
| Temporal  | `mem:{uuid}:ts:{unix_ms}` → `<proto bytes>` | 60 d |

* Lists are **ziplist-encoded** (Valkey default) → O(1) push/pop ([GitHub][1]).
* Graph traversal: `LRANGE mem:{src}:out:*` is avoided—edge type is encoded in the key to keep look-ups O(1).

---

## 4 · Vector Search Path

1. **Ingest**

   ```py
   vec_id = int(uuid.uuid4().int >> 64)  # 64-bit
   index.add_with_ids(np.array([emb], dtype='float32'), np.array([vec_id]))
   r.set(f"vec:{vec_id}", node_uuid)
   ```
2. **Search**

   ```py
   I, D = index.search(query_vec, k=10)  # I = ids
   uuids = r.mget([f"vec:{i}" for i in I[0]])
   ```

*Faiss ID mapping + Redis KV protects against pointer invalidation when index is rebuilt* ([GitHub][10]).

---

## 5 · API Surface (FastAPI)

### 5.1 AAP Endpoints

| Method | Path                    | Payload / Params        |
| ------ | ----------------------- | ----------------------- |
| `PUT`  | `/nodes`                | `Node` proto            |
| `GET`  | `/nodes/{uuid}`         | —                       |
| `GET`  | `/nodes/{uuid}/at/{ts}` | time-travel             |
| `PUT`  | `/edges`                | `{src,dst,type,weight}` |
| `GET`  | `/edges/{src}`          | `type`, `dir`           |
| `POST` | `/semantic_search`      | `{embedding,k}`         |
| `GET`  | `/keyword_search`       | `q`, `k`, `fields`      |
| `POST` | `/summarise`            | `{root_uuid}`           |

### 5.2 MCP Proxy

* `/v1/tools`, `/v1/resources`, `/v1/prompts` simply translate to AAP calls and re-shape to MCP schema json ([GitHub][11]).

---

## 6 · Docker Compose + Healthchecks

```yaml
services:
  valkey:
    image: valkey/valkey:8.1.1-alpine
    command: ["valkey-server","--save","","--appendonly","no"]
    healthcheck:
      test: ["CMD", "valkey-cli","ping"]   # returns PONG
      interval: 10s
      retries: 3
    ports: ["6379:6379"]                   # expose for local debug
  faiss:                                   # stateless side-car
    image: ghcr.io/facebookresearch/faiss-cpu:1.11.0
    command: ["sleep","infinity"]
  ollama:
    image: ollama/ollama:latest
    volumes: ["./models:/root/.ollama/models"]
    ports: ["11434:11434"]
  agramad:
    build: .
    depends_on:
      valkey:
        condition: service_healthy
    environment:
      - VALKEY_URL=redis://valkey:6379
      - FAISS_HOST=faiss
      - OLLAMA_URL=http://ollama:11434
    ports: ["8000:8000"]
```

*`healthcheck` keeps the API container in **“starting”** until Valkey answers `PONG` ([GitHub][12]).*

---

## 7 · Testing & Bench Harness

### 7.1 Unit + Property Tests

```python
from hypothesis import given
@given(node_type=st.sampled_from(["Session","Task","CodeUnit"]))
def test_key_schema_roundtrip(node_type):
    uuid = new_uuid()
    key = make_node_key(uuid)
    assert parse_node_key(key) == uuid
```

### 7.2 Performance Gate

```bash
pytest --benchmark-autosave
pytest-benchmark compare --sort=mean
```

*CI fails if p99 `get_node` > 1 ms or if current mean regresses > 10 %* ([pytest-benchmark][13]).

### 7.3 Load Smoke (k6)

`k6/script.js`:

```js
import http from 'k6/http';
export let options = { vus: 50, duration: '1m' };
export default function () {
  http.get('http://localhost:8000/nodes/seed-0001');
}
```

Run with `docker run --rm -i grafana/k6 run - < k6/script.js` expecting < 1 % errors ([k6.io][14]).

---

## 8 · Summarisation Worker

* **Endpoint:** `POST /summarise {root_uuid}`
* **Flow:**

  1. Gather all `Interaction` nodes under `root_uuid` (DFS).
  2. Chunk to ≤ 8 k tokens; stream into Ollama `/api/chat` with system prompt:

     > “Summarise these interactions for future retrieval …”
  3. Receive markdown; store as a new `SummaryNode`; link with edge `summarises`.
* Ollama call (Python):

```python
import httpx, json
resp = httpx.post(
  f"{OLLAMA}/api/generate",
  json={"model":"qwen3:1.7b","prompt":prompt,"stream":False}
).json()
```

Example repos show similar one-shot summarizers with Qwen-2; adapt for Qwen3 ([GitHub][15], [GitHub][16]).

---

## 9 · TUI Details (Textual)

### 9.1 Screen Layout

```
┌──────── Graph Tree ────────┐┌─ Preview ────────┐
│ Session › Task › …         ││ Markdown / code  │
│ (Keyboard: ↑ ↓ → ←)        │└──────────────────┘
├──────── Neighbors ─────────┤
│ Edge list w/ weights       │
├──────── Command Palette ───┤
│ > _                        │
└────────────────────────────┘
```

* **Tree** uses `Tree[str]`, `DirectoryTree`, or `JSONTree` widgets ([Textual Documentation][9]).
* Global keymap mirrors lazygit:

  | Key       | Action            |
  | --------- | ----------------- |
  | `→` / `←` | Traverse edge     |
  | `s`       | Semantic search   |
  | `/`       | Keyword search    |
  | `t`       | Time-travel input |
  | `p`       | Command palette   |
  | `q`       | Quit              |

Keybinding names align with lazygit’s canonical list for muscle memory ([GitHub][17]).

### 9.2 Code Snippet

```python
class AgramaTUI(App):
    CSS_PATH = "tui.tcss"
    BINDINGS = [("s","semantic_search","Semantic Search"), ("t","time_travel","At Time"), ("q","quit","Quit")]

    def compose(self):
        self.tree = Tree("Memory")
        yield Horizontal(
            self.tree,
            Vertical(Neighbors(), Preview())
        )
```

---

## 10 · CI / CD Pipeline

| Step        | Tool                                              | Cache Strategy                  |
| ----------- | ------------------------------------------------- | ------------------------------- |
| Lint + mypy | ruff, mypy                                        | `--pre-commit`                  |
| Unit tests  | pytest                                            | GitHub cache for `~/.cache/pip` |
| Component   | docker compose up –wait                           | Layered build cache             |
| Bench       | pytest-benchmark json; `pytest-benchmark compare` | Artefact store                  |
| Image       | Buildx multi-arch (linux/amd64, linux/arm64)      | `cache-from`                    |
| Release     | GitHub draft release + OCI push                   | Signed SBOM                     |

---

## 11 · Local Dev Cheatsheet

```bash
# bootstrap
make dev          # spin containers
make seed         # load 10k sample nodes
agrama tui        # open Textual UI
# hacking
make proto        # re-generate gRPC stubs
make test         # full test matrix
make bench        # micro-bench
make load         # k6 100 RPS
# MCP client demo
python -m agrama.demo.get_code_snippet "TypeScript debounce"
```

---

## 12 · Next Actions for Lead Dev

1. **Proto freeze:** lock message IDs before week-2 to avoid breaking stored data.
2. **Implement Valkey pipelines:** use `MULTI/EXEC` for batch edge inserts to hit 10 k ops/s target.
3. **Wire Search fallback:** if `embedding` is missing, default to BM25 only.
4. **Write TUI CSS:** grid layout + dark/light theme toggle (`action_toggle_dark`) ([Textual Documentation][18]).

---

### Key References

Valkey 8.1.1 notes ([GitHub][1]) Faiss 1.11 release ([GitHub][2]) Textual docs ([GitHub][3]) Tree widget guide ([Textual Documentation][9]) Lazygit keybindings ([GitHub][17]) Jina embeddings v3 card ([Hugging Face][5]) Ollama qwen3 model page ([Ollama][6]) MCP spec repo ([GitHub][7]) MCP servers repo ([GitHub][8]) Docker healthcheck recipe ([GitHub][12]) Pytest-benchmark compare docs ([pytest-benchmark][13]) k6 quickstart docs ([k6.io][14]) Faiss ID mapping example ([GitHub][10]) Ollama summariser examples ([GitHub][15])

[1]: https://github.com/valkey-io/valkey/releases "Releases · valkey-io/valkey · GitHub"
[2]: https://github.com/facebookresearch/faiss/releases "Releases · facebookresearch/faiss · GitHub"
[3]: https://github.com/Textualize/textual "GitHub - Textualize/textual: The lean application framework for Python.  Build sophisticated user interfaces with a simple Python API. Run your apps in the terminal and a web browser."
[4]: https://www.theverge.com/news/669298/microsoft-windows-ai-foundry-mcp-support?utm_source=chatgpt.com "Windows is getting support for the 'USB-C of AI apps'"
[5]: https://huggingface.co/jinaai/jina-embeddings-v3?utm_source=chatgpt.com "jinaai/jina-embeddings-v3 - Hugging Face"
[6]: https://ollama.com/library/qwen3?utm_source=chatgpt.com "qwen3 - Ollama"
[7]: https://github.com/modelcontextprotocol?utm_source=chatgpt.com "Model Context Protocol - GitHub"
[8]: https://github.com/modelcontextprotocol/servers?utm_source=chatgpt.com "modelcontextprotocol/servers: Model Context Protocol ... - GitHub"
[9]: https://textual.textualize.io/widgets/tree/?utm_source=chatgpt.com "Tree - Textual"
[10]: https://github.com/facebookresearch/faiss/wiki/getting-started "Getting started · facebookresearch/faiss Wiki · GitHub"
[11]: https://github.com/modelcontextprotocol/modelcontextprotocol?utm_source=chatgpt.com "Specification and documentation for the Model Context Protocol"
[12]: https://github.com/peter-evans/docker-compose-healthcheck "GitHub - peter-evans/docker-compose-healthcheck: How to wait for container X before starting Y using docker-compose healthcheck"
[13]: https://pytest-benchmark.readthedocs.io/en/latest/usage.html?utm_source=chatgpt.com "Usage - pytest-benchmark 5.1.0 documentation"
[14]: https://k6.io/docs/examples/tutorials/get-started-with-k6/?utm_source=chatgpt.com "Get started with k6 | Grafana k6 documentation"
[15]: https://github.com/revant-kumar/ollama-mini-project?utm_source=chatgpt.com "A mini CLI project to summarize text using Ollama Qwen2-0.5B LLM ..."
[16]: https://github.com/ollama/ollama?utm_source=chatgpt.com "ollama/ollama: Get up and running with Llama 3.3, DeepSeek-R1 ..."
[17]: https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md?plain=1&utm_source=chatgpt.com "lazygit/docs/keybindings/Keybindings_en.md at master - GitHub"
[18]: https://textual.textualize.io/styles/layout/?utm_source=chatgpt.com "Layout - Textual"

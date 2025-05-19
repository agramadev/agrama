# Agrama Project TODO

## TODO Specification & Style Guide

- **Platform**: develop for macOS, Linux, and Windows 11 (with MCP support) as specified in SPECS.md §0.
- **Development Workflow**: follow test/benchmark-first workflow for each feature:
  1. Create functional specification in a `SPEC.md` file within the feature folder (e.g., `agrama/api/SPEC.md`).
  2. Write automated tests covering the desired behavior.
  3. Implement code to satisfy tests.
  4. Benchmark and optimize to meet performance targets.
- **Task entries**: use GitHub-flavored Markdown task lists:
  - `- [ ]` for open tasks
  - `- [x]` for completed tasks
- **Priority tags**: append `(P1)`, `(P2)`, `(P3)`, etc., to task descriptions:
  - `P1`: critical / must-have
  - `P2`: important
  - `P3`: nice-to-have
- **Effort levels**: append `(E1)`, `(E2)`, `(E3)` to indicate estimated effort:
  - `E1`: small task (hours)
  - `E2`: medium task (1-2 days)
  - `E3`: large task (3+ days)
- **Phases**: group tasks under `## Phase <n>: <phase name>` headings in ascending order.
- **Specification references**: link tasks to `SPECS.md` section numbers, e.g., `SPECS.md §3`.

## Phases & Tasks

### Phase 1: Project Setup & Dependencies

- [x] Create project directory layout as specified (P1, E1, SPECS.md §2)
  - `agrama/` package with subdirectories: `api/`, `db/`, `vector/`, `proto/`, `summariser/`, `tests/`
  - Root-level directories: `tui/`, `docker/`, `bench/`, `k6/`
- [x] Set up development environment with Docker Compose (P1, E1, SPECS.md §6)
- [x] Pin Valkey to 8.1.1 in Docker Compose (P1, E1, SPECS.md §1)
- [x] Pin Faiss to 1.11.0 in Docker Compose (P1, E1, SPECS.md §1)
- [x] Configure Ollama to use `qwen3:1.7b` (P1, E1, SPECS.md §1)
- [x] Set up Python dependencies including Textual 0.52 (P1, E1, SPECS.md §1)
- [x] Add `jina-embeddings-v3` for multilingual embeddings (P1, E1, SPECS.md §1)
- [x] Create `Makefile` with basic commands (dev, test, proto) (P1, E1, SPECS.md §11)
- [x] Create `make.bat` for Windows compatibility (P2, E1, SPECS.md §12)

### Phase 2: Core Data Model & Protobuf

- [x] Create functional spec in `agrama/proto/SPEC.md` (P1, E1, SPECS.md §3)
- [x] Write tests for Node protobuf message and key schema conventions (P1, E1, SPECS.md §3)
- [x] **Proto freeze**: lock message IDs before implementation to avoid breaking stored data (P1, E1, SPECS.md §12)
- [x] Implement Node protobuf message with fields: uuid, type, created_at, updated_at, content, embedding (P1, E2, SPECS.md §3.1)
- [x] Set up `buf` for protobuf compilation (P1, E1, SPECS.md §2)
- [x] Implement key schema conventions for nodes, edges, and temporal data (P1, E2, SPECS.md §3.2)
- [x] Write property tests for key schema roundtrip using Hypothesis (P1, E1, SPECS.md §7.1)

### Phase 3: Valkey Database Integration

- [x] Create functional spec in `agrama/db/SPEC.md` (P1, E1, SPECS.md §3)
- [ ] Write tests for Valkey client operations (P1, E1, SPECS.md §3)
- [x] Implement Valkey client wrapper with connection pooling (P1, E2, SPECS.md §3)
- [x] Implement node CRUD operations (P1, E2, SPECS.md §3)
- [x] Implement edge operations with ziplist encoding for O(1) push/pop (P1, E2, SPECS.md §3.2)
- [x] **Implement Valkey pipelines**: use `MULTI/EXEC` for batch edge inserts to hit 10k ops/s target (P1, E2, SPECS.md §12)
- [ ] Add time-travel query support for historical node states (P2, E2, SPECS.md §5.1)

### Phase 4: Vector Search Implementation

- [x] Create functional spec in `agrama/vector/SPEC.md` (P1, E1, SPECS.md §4)
- [ ] Write tests for vector ingestion and search flows (P1, E1, SPECS.md §4)
- [x] Implement Faiss wrapper with connection to Faiss container (P1, E2, SPECS.md §4)
- [x] Implement ingestion flow: generate 64-bit vec_id, index.add_with_ids, and store mapping in Valkey (P1, E2, SPECS.md §4)
- [x] Implement search flow: perform index.search and map IDs back to UUIDs via Valkey (P1, E2, SPECS.md §4)
- [x] **Wire search fallback**: default to BM25 if embedding is missing (P1, E2, SPECS.md §12)
- [ ] Add benchmarks for vector search performance (P2, E1, SPECS.md §7.2)

### Phase 5: API Surface Implementation

- [x] Create functional spec in `agrama/api/SPEC.md` (P1, E1, SPECS.md §5)
- [ ] Write tests for AAP endpoints (P1, E2, SPECS.md §5.1)
  - `PUT /nodes`, `GET /nodes/{uuid}`, `GET /nodes/{uuid}/at/{ts}`
  - `PUT /edges`, `GET /edges/{src}`
  - `POST /semantic_search`, `GET /keyword_search`
  - `POST /summarise`
- [x] Implement FastAPI router for AAP endpoints (P1, E2, SPECS.md §5.1)
- [ ] Write tests for MCP proxy endpoints (P1, E1, SPECS.md §5.2)
  - `/v1/tools`, `/v1/resources`, `/v1/prompts`
- [x] Implement MCP proxy endpoints with translation to AAP calls (P1, E2, SPECS.md §5.2)
- [x] Ensure MCP spec compliance (v0.13) (P1, E2, SPECS.md §1)
- [ ] Add API documentation with examples (P2, E2, SPECS.md §12)

### Phase 6: Docker Compose & Deployment

- [ ] Write `docker-compose.yml` with services (valkey, faiss, ollama, agramad) and ports (P1, E1, SPECS.md §6)
- [ ] Add healthcheck for valkey (`valkey-cli ping`) (P1, E1, SPECS.md §6)
- [ ] Configure service dependencies to ensure proper startup order (P1, E1, SPECS.md §6)
- [ ] Configure environment variables for agramad: `VALKEY_URL`, `FAISS_HOST`, `OLLAMA_URL` (P1, E1, SPECS.md §6)
- [ ] Create Dockerfile for agramad service (P1, E1, SPECS.md §6)
- [ ] Add volume for Ollama models (P1, E1, SPECS.md §6)
- [ ] Create seed script to load sample nodes (P2, E2, SPECS.md §11)

### Phase 7: Testing & Benchmarking Framework

- [ ] Set up pytest with Hypothesis for property-based testing (P1, E1, SPECS.md §7.1)
- [ ] Configure pytest-benchmark for autosave and performance compare (P1, E1, SPECS.md §7.2)
- [ ] Create benchmark comparison script (P1, E1, SPECS.md §7.2)
- [ ] Enforce performance gate: fail CI if p99 latency >1ms or mean regresses >10% (P1, E2, SPECS.md §7.2)
- [ ] Add k6 load test script for 50 VUs over 1 minute (P2, E1, SPECS.md §7.3)
- [ ] Create benchmark documentation with baseline results (P2, E1, SPECS.md §12)

### Phase 8: Summarisation Worker

- [x] Create functional spec in `agrama/summariser/SPEC.md` (P1, E1, SPECS.md §8)
- [ ] Write tests for summarisation flow (P1, E1, SPECS.md §8)
- [x] Implement Ollama client wrapper (P1, E1, SPECS.md §8)
- [ ] Implement DFS algorithm to gather all Interaction nodes under root_uuid (P1, E2, SPECS.md §8)
- [ ] Implement text chunking to ≤8k tokens (P1, E1, SPECS.md §8)
- [ ] Implement Ollama `/api/generate` call with system prompt (P1, E1, SPECS.md §8)
- [ ] Store generated summary as a new SummaryNode with "summarises" edge (P1, E1, SPECS.md §8)
- [ ] Add benchmarks for summarisation performance (P2, E1, SPECS.md §7.2)

### Phase 9: TUI Implementation

- [x] Create functional spec in `tui/SPEC.md` (P1, E1, SPECS.md §9)
- [ ] Write tests for TUI components and interactions (P1, E2, SPECS.md §9)
- [x] Implement main TUI layout with Graph Tree, Neighbors, and Preview pane (P2, E2, SPECS.md §9.1)
- [x] Implement Tree widget for graph navigation (P2, E2, SPECS.md §9.1)
- [x] Apply keybindings matching lazygit muscle memory (P2, E1, SPECS.md §9.1)
  - Arrows for traversal, `s` for semantic search, `/` for keyword search
  - `t` for time-travel, `p` for command palette, `q` for quit
- [x] **Write TUI CSS**: grid layout + dark/light theme toggle (`action_toggle_dark`) (P2, E1, SPECS.md §12)
- [ ] Create user guide with screenshots and usage examples (P2, E2, SPECS.md §12)

### Phase 10: CI/CD Pipeline

- [ ] Set up linting with ruff (P1, E1, SPECS.md §10)
- [ ] Set up type-checking with mypy (P1, E1, SPECS.md §10)
- [ ] Configure GitHub Actions for unit tests (P1, E1, SPECS.md §10)
- [ ] Add component tests with docker compose (P1, E1, SPECS.md §10)
- [ ] Set up benchmark comparison in CI (P2, E1, SPECS.md §10)
- [ ] Configure multi-arch builds (linux/amd64, linux/arm64) with Buildx (P2, E2, SPECS.md §10)
- [ ] Set up GitHub release workflow with OCI push and SBOM (P2, E2, SPECS.md §10)
- [ ] Add caching strategies for pip, Docker layers (P2, E1, SPECS.md §10)

### Phase 11: Local Development Experience

- [ ] Document local development commands in README.md (P2, E1, SPECS.md §11)
  - `make dev` - spin up containers
  - `make seed` - load sample data
  - `agrama tui` - open Textual UI
  - `make proto` - regenerate gRPC stubs
  - `make test` - run test suite
  - `make bench` - run benchmarks
  - `make load` - run k6 load test
- [ ] Create Python demo script for MCP client (P2, E1, SPECS.md §11)
- [ ] Add developer guide with architecture overview (P2, E2, SPECS.md §12)
- [ ] Create troubleshooting guide with common issues (P3, E1, SPECS.md §12)

### Phase 12: Documentation

- [x] Create documentation structure in `/docs` folder (P1, E1)
- [x] Set up MkDocs with Material theme for documentation generation (P1, E1)
- [ ] Write installation guide with detailed setup instructions (P1, E1, SPECS.md §12)
- [ ] Document data model and key schema with diagrams (P1, E2, SPECS.md §12)
- [ ] Create API reference documentation (P1, E2, SPECS.md §12)
- [ ] Document performance benchmarks and optimization guidelines (P2, E1, SPECS.md §12)
- [ ] Write deployment guide for production environments (P2, E1, SPECS.md §12)
- [ ] Add contribution guidelines with code style and PR process (P3, E1, SPECS.md §12)
- [ ] Configure GitHub Pages for hosting the documentation (P3, E1, SPECS.md §12)

# Developer Guide

This guide provides information for developers who want to contribute to or extend Agrama.

## Architecture Overview

Agrama follows a modular architecture with the following components:

- **API Layer**: FastAPI-based REST API with AAP and MCP endpoints
- **Database Layer**: Valkey client (valkey-py) and graph helpers
- **Vector Search**: Faiss wrapper for embedding storage and retrieval
- **Summarization**: Ollama client for LLM-powered summarization
- **TUI**: Textual-based terminal user interface

## Directory Structure

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

## Development Environment Setup

### Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Make (for using the Makefile)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agrama.git
   cd agrama
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

5. Start the development containers:
   ```bash
   make dev
   ```

## Development Workflow

Agrama follows a test-driven development approach:

1. Create a functional specification in a `SPEC.md` file within the feature folder
2. Write automated tests covering the desired behavior
3. Implement code to satisfy the tests

### Common Development Tasks

```bash
# Start development containers
make dev

# Load sample data
make seed

# Run tests
make test

# Run benchmarks
make bench

# Run load tests
make load

# Generate protocol buffers
make proto
```

## Key Components

### Data Model

The core data model is defined in Protocol Buffers:

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

### Key Schema

Agrama uses a specific key schema for storing nodes and edges in Valkey:

| Purpose   | Pattern                                     | TTL  |
| --------- | ------------------------------------------- | ---- |
| Node blob | `mem:{uuid}` → `<proto bytes>`              | ∞    |
| Out edges | `mem:{src}:out:{etype}` → `[dst1 … dstN]`   | ∞    |
| In edges  | `mem:{dst}:in:{etype}`  → `[src1 … srcN]`   | ∞    |
| Temporal  | `mem:{uuid}:ts:{unix_ms}` → `<proto bytes>` | 60 d |

### Vector Search

The vector search implementation uses Faiss with a mapping to UUIDs stored in Valkey:

```python
# Ingest
vec_id = int(uuid.uuid4().int >> 64)  # 64-bit
index.add_with_ids(np.array([emb], dtype='float32'), np.array([vec_id]))
r.set(f"vec:{vec_id}", node_uuid)

# Search
I, D = index.search(query_vec, k=10)  # I = ids
uuids = r.mget([f"vec:{i}" for i in I[0]])
```

## Testing

Agrama uses pytest for unit tests and property-based testing with Hypothesis:

```python
from hypothesis import given
@given(node_type=st.sampled_from(["Session","Task","CodeUnit"]))
def test_key_schema_roundtrip(node_type):
    uuid = new_uuid()
    key = make_node_key(uuid)
    assert parse_node_key(key) == uuid
```

Performance testing is done with pytest-benchmark:

```bash
pytest --benchmark-autosave
pytest-benchmark compare --sort=mean
```

## Contributing Guidelines

Please see the [Contributing Guide](contributing.md) for details on our code of conduct and the process for submitting pull requests.

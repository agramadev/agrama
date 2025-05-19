# Agrama

Agrama is a local micro-stack for knowledge management and retrieval, combining key-value storage, vector search, and LLM-powered summarization in a single, easy-to-deploy package.

## Overview

Agrama provides a comprehensive solution for storing, retrieving, and analyzing structured and unstructured data with:

- **Valkey 8.1** for key-value storage and graph relationships
- **Faiss 1.11** for high-performance vector search
- **Ollama** running `qwen3:1.7b` for text summarization
- **FastAPI MCP server** for API access
- **Textual-based TUI** for interactive exploration

Get sub-millisecond direct lookups, <50ms semantic search, and a simple deployment experience with `docker compose up`.

## Features

- **Graph-based Knowledge Storage**: Store nodes and relationships with efficient key schema
- **Vector Search**: Semantic search capabilities with Faiss
- **Text Summarization**: LLM-powered summarization of content
- **MCP Protocol Support**: Compatible with the Model Context Protocol
- **Interactive TUI**: Explore your knowledge graph with a terminal UI
- **High Performance**: Sub-millisecond lookups and fast semantic search
- **Easy Deployment**: Simple Docker Compose setup

## Installation

### Prerequisites

- Docker and Docker Compose
- Python 3.10+

### Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agrama.git
   cd agrama
   ```

2. Start the services:
   ```bash
   docker compose up -d
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the TUI:
   ```bash
   agrama tui
   ```

## Development

### Setup Development Environment

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
```

### Documentation

The project documentation is built using MkDocs with the Material theme. To work with the documentation:

```bash
# Install documentation dependencies
pip install -r requirements.txt

# Serve the documentation locally
mkdocs serve

# Build the documentation
mkdocs build
```

The documentation is available at [https://yourusername.github.io/agrama/](https://yourusername.github.io/agrama/) or locally at http://127.0.0.1:8000/ when running `mkdocs serve`.

### Development Commands

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

## API Endpoints

### AAP Endpoints

| Method | Path                    | Description                      |
|--------|-------------------------|----------------------------------|
| `PUT`  | `/nodes`                | Create or update a node          |
| `GET`  | `/nodes/{uuid}`         | Get a node by UUID               |
| `GET`  | `/nodes/{uuid}/at/{ts}` | Get a node at a specific time    |
| `PUT`  | `/edges`                | Create an edge between nodes     |
| `GET`  | `/edges/{src}`          | Get edges from a source node     |
| `POST` | `/semantic_search`      | Search nodes by vector similarity |
| `GET`  | `/keyword_search`       | Search nodes by keywords         |
| `POST` | `/summarise`            | Generate a summary for a subgraph |

### MCP Proxy

The MCP proxy endpoints (`/v1/tools`, `/v1/resources`, `/v1/prompts`) translate AAP calls to the MCP schema.

## Architecture

Agrama follows a modular architecture with the following components:

- **API Layer**: FastAPI-based REST API with AAP and MCP endpoints
- **Database Layer**: Valkey client (valkey-py) and graph helpers
- **Vector Search**: Faiss wrapper for embedding storage and retrieval
- **Summarization**: Ollama client for LLM-powered summarization
- **TUI**: Textual-based terminal user interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

All rights reserved. See [LICENSE](LICENSE) for more information.

# Installation Guide

This guide will walk you through the process of installing and configuring Agrama and its dependencies.

## Prerequisites

Before installing Agrama, ensure you have the following prerequisites installed:

- **Docker** and **Docker Compose** (version 2.0 or higher)
- **Python** 3.10 or higher
- **Git** for cloning the repository

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agrama.git
cd agrama
```

### 2. Set Up Python Environment

```bash
# Create and activate a virtual environment (using uv)
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv install
```

### 3. Start the Docker Services

```bash
# Start all services in detached mode
docker compose up -d
```

This command will start the following services:
- **Valkey**: Key-value store and graph database
- **Faiss**: Vector search engine
- **Ollama**: LLM service for summarization
- **Agramad**: The Agrama API server

### 4. Verify Installation

To verify that all services are running correctly:

```bash
docker compose ps
```

You should see all services in the "running" state.

### 5. Load Sample Data (Optional)

To load sample data for testing:

```bash
make seed
```

## Component-Specific Configuration

### Valkey Configuration

Valkey runs on port 6379 by default. You can customize its configuration by editing the `docker-compose.yml` file.

### Faiss Configuration

Faiss runs as a stateless sidecar service. No additional configuration is typically needed.

### Ollama Configuration

Ollama runs on port 11434 by default. To use a different model:

1. Edit the `docker-compose.yml` file
2. Change the `OLLAMA_MODEL` environment variable

### API Server Configuration

The API server runs on port 8000 by default. You can configure it using environment variables:

- `VALKEY_URL`: URL for the Valkey instance
- `FAISS_HOST`: Hostname for the Faiss service
- `OLLAMA_URL`: URL for the Ollama service

## Troubleshooting

### Common Issues

#### Services Not Starting

If services fail to start, check the logs:

```bash
docker compose logs
```

#### Connection Errors

If you encounter connection errors, ensure all services are running and that the configuration points to the correct hostnames and ports.

## Next Steps

After installation, you can:

- Explore the [API Documentation](api/index.md)
- Learn how to use the [TUI](user/index.md)
- Check out the [Developer Guide](developer/index.md) for extending Agrama

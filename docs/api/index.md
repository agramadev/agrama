# API Documentation

This section provides detailed information about the Agrama API endpoints, request/response formats, and usage examples.

## API Overview

Agrama provides two sets of API endpoints:

1. **AAP (Agrama Application Protocol)** - Core functionality for node and edge management, semantic search, and summarization
2. **MCP (Model Context Protocol)** - Proxy endpoints that translate AAP calls to the MCP schema

## Base URL

By default, the API server runs at:

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication for local development. For production deployments, refer to the [Deployment Guide](../deployment/index.md) for security recommendations.

## AAP Endpoints

### Node Management

- [PUT /nodes](nodes.md#create-node) - Create or update a node
- [GET /nodes/{uuid}](nodes.md#get-node) - Get a node by UUID
- [GET /nodes/{uuid}/at/{ts}](nodes.md#get-node-at-time) - Get a node at a specific time

### Edge Management

- [PUT /edges](edges.md#create-edge) - Create an edge between nodes
- [GET /edges/{src}](edges.md#get-edges) - Get edges from a source node

### Search

- [POST /semantic_search](search.md#semantic-search) - Search nodes by vector similarity
- [GET /keyword_search](search.md#keyword-search) - Search nodes by keywords

### Summarization

- [POST /summarise](summarization.md#summarize) - Generate a summary for a subgraph

## MCP Proxy Endpoints

- [GET /v1/tools](mcp.md#tools) - Get available tools
- [GET /v1/resources](mcp.md#resources) - Get available resources
- [GET /v1/prompts](mcp.md#prompts) - Get available prompts

## Error Handling

All API endpoints return standard HTTP status codes:

- `200 OK` - The request was successful
- `400 Bad Request` - The request was invalid
- `404 Not Found` - The requested resource was not found
- `500 Internal Server Error` - An error occurred on the server

Error responses include a JSON body with details:

```json
{
  "error": "Error message",
  "details": "Additional details about the error"
}
```

## Rate Limiting

The API currently does not implement rate limiting for local development. For production deployments, refer to the [Deployment Guide](../deployment/index.md) for recommendations.

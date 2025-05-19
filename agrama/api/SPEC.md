# API Surface Implementation Specification

## Overview

This document specifies the API surface for Agrama, which provides both Agrama API Protocol (AAP) endpoints and Model Context Protocol (MCP) proxy endpoints. The API is implemented using FastAPI and provides a RESTful interface for interacting with the Agrama system.

## AAP Endpoints

### Node Operations

#### PUT /nodes

Create or update a node.

**Request:**
```json
{
  "uuid": "optional-uuid",
  "type": "Session",
  "content": "Node content",
  "embedding": [0.1, 0.2, 0.3, ...]
}
```

**Response:**
```json
{
  "uuid": "node-uuid",
  "type": "Session",
  "created_at": 1625097600000,
  "updated_at": 1625097600000,
  "content": "Node content",
  "embedding": [0.1, 0.2, 0.3, ...]
}
```

#### GET /nodes/{uuid}

Get a node by UUID.

**Response:**
```json
{
  "uuid": "node-uuid",
  "type": "Session",
  "created_at": 1625097600000,
  "updated_at": 1625097600000,
  "content": "Node content",
  "embedding": [0.1, 0.2, 0.3, ...]
}
```

#### GET /nodes/{uuid}/at/{ts}

Get a node by UUID at a specific time.

**Response:**
```json
{
  "uuid": "node-uuid",
  "type": "Session",
  "created_at": 1625097600000,
  "updated_at": 1625097600000,
  "content": "Node content",
  "embedding": [0.1, 0.2, 0.3, ...]
}
```

### Edge Operations

#### PUT /edges

Create an edge between two nodes.

**Request:**
```json
{
  "src": "source-uuid",
  "dst": "destination-uuid",
  "type": "contains",
  "weight": 1.0
}
```

**Response:**
```json
{
  "src": "source-uuid",
  "dst": "destination-uuid",
  "type": "contains",
  "weight": 1.0
}
```

#### GET /edges/{src}

Get edges for a node.

**Query Parameters:**
- `edge_type`: The type of the edge (optional)
- `direction`: The direction of the edge, either "out" or "in" (default: "out")

**Response:**
```json
{
  "edges": [
    {
      "src": "source-uuid",
      "dst": "destination-uuid",
      "type": "contains",
      "weight": 1.0
    },
    ...
  ]
}
```

### Search Operations

#### POST /semantic_search

Search for nodes by vector similarity.

**Request:**
```json
{
  "embedding": [0.1, 0.2, 0.3, ...],
  "k": 10
}
```

**Response:**
```json
[
  {
    "uuid": "node-uuid",
    "type": "Session",
    "created_at": 1625097600000,
    "updated_at": 1625097600000,
    "content": "Node content",
    "distance": 0.1
  },
  ...
]
```

#### GET /keyword_search

Search for nodes by keywords.

**Query Parameters:**
- `q`: The search query
- `k`: The number of results to return (default: 10)
- `fields`: The fields to search in, comma-separated (optional)

**Response:**
```json
[
  {
    "uuid": "node-uuid",
    "type": "Session",
    "created_at": 1625097600000,
    "updated_at": 1625097600000,
    "content": "Node content",
    "score": 0.9
  },
  ...
]
```

### Summarisation Operations

#### POST /summarise

Generate a summary for a subgraph.

**Request:**
```json
{
  "root_uuid": "root-uuid"
}
```

**Response:**
```json
{
  "status": "ok",
  "message": "Summarisation for node root-uuid started"
}
```

## MCP Proxy Endpoints

### GET /v1/tools

Get available tools.

**Response:**
```json
{
  "tools": [
    {
      "name": "agrama_search",
      "description": "Search for nodes in the Agrama knowledge graph",
      "input_schema": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "The search query"
          },
          "k": {
            "type": "integer",
            "description": "The number of results to return",
            "default": 10
          }
        },
        "required": ["query"]
      }
    },
    ...
  ]
}
```

### POST /v1/tools/{tool_name}

Call a tool.

**Request:**
```json
{
  "query": "search query",
  "k": 10
}
```

**Response:**
```json
{
  "results": [
    {
      "uuid": "node-uuid",
      "type": "Session",
      "content": "Node content",
      "score": 0.9
    },
    ...
  ]
}
```

### GET /v1/resources

Get available resources.

**Response:**
```json
{
  "resources": []
}
```

### GET /v1/prompts

Get available prompts.

**Response:**
```json
{
  "prompts": []
}
```

## Error Handling

All endpoints return appropriate HTTP status codes and error messages:

- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Authentication and Authorization

The API does not currently implement authentication or authorization. This will be added in a future version.

## Rate Limiting

The API does not currently implement rate limiting. This will be added in a future version.

## CORS

The API supports Cross-Origin Resource Sharing (CORS) with the following configuration:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Future Enhancements

- Add authentication and authorization
- Add rate limiting
- Add API versioning
- Add OpenAPI documentation
- Add support for WebSockets for real-time updates

# Valkey Database Integration Specification

## Overview

This document specifies the integration between Agrama and Valkey, a Redis-compatible key-value store. The integration provides a graph database abstraction on top of Valkey's key-value capabilities, with efficient key schema conventions for nodes, edges, and temporal data.

## Key Schema Conventions

### Node Storage

Nodes are stored as serialized Protocol Buffer messages with the following key pattern:

```
mem:{uuid} → <proto bytes>
```

Where:
- `{uuid}` is the UUID of the node
- `<proto bytes>` is the serialized Protocol Buffer message

### Edge Storage

Edges are stored as lists of node UUIDs with the following key patterns:

```
mem:{src}:out:{etype} → [dst1 … dstN]   # Outgoing edges
mem:{dst}:in:{etype}  → [src1 … srcN]   # Incoming edges
```

Where:
- `{src}` is the UUID of the source node
- `{dst}` is the UUID of the destination node
- `{etype}` is the type of the edge
- The value is a list of node UUIDs

Lists are ziplist-encoded (Valkey default) for O(1) push/pop operations.

### Temporal Data

Historical node states are stored with the following key pattern:

```
mem:{uuid}:ts:{unix_ms} → <proto bytes>
```

Where:
- `{uuid}` is the UUID of the node
- `{unix_ms}` is the timestamp in milliseconds
- `<proto bytes>` is the serialized Protocol Buffer message

Temporal data has a TTL of 60 days.

### Vector Mapping

Vector IDs are mapped to node UUIDs with the following key pattern:

```
vec:{vec_id} → {uuid}
```

Where:
- `{vec_id}` is the vector ID (64-bit integer)
- `{uuid}` is the UUID of the node

## Client Interface

### Connection Management

The `ValkeyClient` class provides connection pooling for efficient access to the Valkey server:

```python
client = ValkeyClient(url="redis://localhost:6379")
```

If the URL is not provided, it uses the `VALKEY_URL` environment variable or falls back to `redis://localhost:6379`.

### Node Operations

```python
# Get a node
node_data = client.get_node(uuid)

# Set a node
client.set_node(uuid, node_data)

# Get a node at a specific time
node_data = client.get_node_at_time(uuid, timestamp)
```

### Edge Operations

```python
# Add an edge
client.add_edge(src, dst, edge_type, direction="out")

# Get edges
edges = client.get_edges(uuid, edge_type, direction="out")
```

### Vector Mapping Operations

```python
# Set a vector mapping
client.set_vector_mapping(vec_id, uuid)

# Get a vector mapping
uuid = client.get_vector_mapping(vec_id)

# Get multiple vector mappings
uuids = client.get_vector_mappings([vec_id1, vec_id2, ...])
```

## Transaction Support

For batch operations, Valkey's `MULTI/EXEC` commands are used to ensure atomicity:

```python
# Start a transaction
pipeline = client.client.pipeline()

# Add operations to the transaction
pipeline.set(key1, value1)
pipeline.set(key2, value2)

# Execute the transaction
results = pipeline.execute()
```

## Performance Considerations

- Node lookups are O(1) operations
- Edge traversal is O(1) for a specific edge type
- Lists are ziplist-encoded for O(1) push/pop operations
- Batch operations use `MULTI/EXEC` for improved performance

## Error Handling

The client handles connection errors and retries operations when appropriate. If a connection cannot be established, the client returns `None` for get operations and `False` for set operations.

## Future Enhancements

- Implement a cache layer for frequently accessed nodes
- Add support for edge properties
- Implement a query language for complex graph traversals

# Vector Search Implementation Specification

## Overview

This document specifies the vector search implementation for Agrama, which uses Faiss for efficient similarity search of high-dimensional vectors. The implementation provides a clean interface for adding, searching, and managing vectors, with integration to the Valkey database for mapping vector IDs to node UUIDs.

## Vector Search Path

### Ingest Flow

1. Generate a 64-bit vector ID from a UUID:
   ```python
   vec_id = int(uuid.uuid4().int >> 64)  # 64-bit
   ```

2. Add the vector to the Faiss index:
   ```python
   index.add_with_ids(np.array([embedding], dtype='float32'), np.array([vec_id]))
   ```

3. Store the mapping from vector ID to node UUID in Valkey:
   ```python
   db.set(f"vec:{vec_id}", node_uuid)
   ```

### Search Flow

1. Search the Faiss index for similar vectors:
   ```python
   I, D = index.search(query_vec, k=10)  # I = ids, D = distances
   ```

2. Map the vector IDs back to node UUIDs using Valkey:
   ```python
   uuids = db.mget([f"vec:{i}" for i in I[0]])
   ```

## Faiss Index Configuration

The default index is `IndexFlatIP` (Inner Product) for cosine similarity, wrapped with `IndexIDMap` for ID mapping:

```python
index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
index_id_map = faiss.IndexIDMap(index)
```

For larger datasets, more efficient indexes like `IndexIVFFlat` or `IndexHNSW` can be used.

## Client Interface

### Initialization

The `FaissClient` class provides a wrapper for the Faiss index:

```python
client = FaissClient(dimension=1024, host="localhost")
```

If the host is not provided, it uses the `FAISS_HOST` environment variable or falls back to `localhost`.

### Vector Operations

```python
# Add a vector
vec_id = client.add(embedding)

# Search for similar vectors
vec_ids, distances = client.search(embedding, k=10)

# Remove a vector
client.remove(vec_id)

# Reset the index
client.reset()

# Save the index to a file
client.save(path)

# Load the index from a file
client.load(path)
```

## Integration with Valkey

The vector search implementation integrates with Valkey for mapping vector IDs to node UUIDs:

1. When a vector is added to the index, the mapping from vector ID to node UUID is stored in Valkey.
2. When searching for similar vectors, the vector IDs are mapped back to node UUIDs using Valkey.

This approach protects against pointer invalidation when the index is rebuilt.

## Fallback to Keyword Search

If a node does not have an embedding, the search falls back to keyword search using BM25:

```python
if not embedding:
    # Fall back to keyword search
    return keyword_search(query, k)
```

## Performance Considerations

- Vector search is optimized for sub-50ms response times
- Vectors are normalized to unit length for cosine similarity
- The index is memory-mapped for efficient access
- Batch operations are used for improved performance

## Error Handling

The client handles index errors and retries operations when appropriate. If an operation fails, the client returns appropriate error codes or raises exceptions.

## Future Enhancements

- Implement quantization for reduced memory usage
- Add support for multiple indexes for different vector types
- Implement a hybrid search combining vector and keyword search
- Add support for incremental index updates

# Summarisation Worker Specification

## Overview

This document specifies the summarisation worker for Agrama, which uses Ollama running `qwen3:1.7b` to generate summaries of subgraphs in the knowledge graph. The worker traverses the graph, collects relevant nodes, and generates a summary that is stored as a new node in the graph.

## Summarisation Flow

1. Receive a request to summarise a subgraph with a root UUID.
2. Gather all `Interaction` nodes under the root UUID using Depth-First Search (DFS).
3. Extract text from each node and chunk it to ≤8k tokens.
4. Stream the text into Ollama `/api/generate` with a system prompt.
5. Receive the generated summary as markdown.
6. Store the summary as a new `SummaryNode` in the graph.
7. Create an edge from the summary node to the root node with type `summarises`.

## Ollama Client Interface

### Initialization

The `OllamaClient` class provides a wrapper for the Ollama API:

```python
client = OllamaClient(url="http://localhost:11434", model="qwen3:1.7b")
```

If the URL is not provided, it uses the `OLLAMA_URL` environment variable or falls back to `http://localhost:11434`.

### Generation Methods

```python
# Generate text
response = await client.generate(prompt, system_prompt=None, stream=False)

# Chat with the model
response = await client.chat(messages, system_prompt=None, stream=False)

# Summarise text
summary = await client.summarise(text, max_tokens=8000)
```

## DFS Algorithm

The DFS algorithm traverses the graph to gather all `Interaction` nodes under a root UUID:

```python
async def gather_interaction_nodes(root_uuid, db):
    visited = set()
    result = []

    async def dfs(uuid):
        if uuid in visited:
            return

        visited.add(uuid)

        # Get the node
        node_data = db.get_node(uuid)
        if not node_data:
            return

        # Parse the node
        node = Node()
        node.ParseFromString(node_data)

        # If it's an Interaction node, add it to the result
        if node.type == "Interaction":
            result.append(node_data)

        # Get outgoing edges
        edges = db.get_edges(uuid, "contains", "out")

        # Recursively visit children
        for dst in edges:
            await dfs(dst)

    await dfs(root_uuid)
    return result
```

## Text Chunking

The text chunking algorithm splits the text into chunks of ≤8k tokens:

```python
def chunk_text(text, max_tokens=8000):
    # Rough estimate: 1 token ≈ 4 characters
    max_chars = max_tokens * 4

    # Split the text into chunks
    chunks = []
    for i in range(0, len(text), max_chars):
        chunks.append(text[i:i+max_chars])

    return chunks
```

## System Prompt

The system prompt for summarisation:

```
Summarise these interactions for future retrieval. Be concise but comprehensive. Focus on key points, decisions, and action items. Use markdown formatting for structure.
```

## Ollama API Call

The Ollama API call for generation:

```python
async def generate(self, prompt, system_prompt=None, stream=False):
    url = f"{self.url}/api/generate"

    payload = {
        "model": self.model,
        "prompt": prompt,
        "stream": stream,
    }

    if system_prompt:
        payload["system"] = system_prompt

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()
```

## Summary Node Creation

The summary node is created and stored in the graph:

```python
# Create a new SummaryNode
summary_node = Node()
summary_node.uuid = str(uuid.uuid4())
summary_node.type = "Summary"
summary_node.created_at = int(time.time() * 1000)
summary_node.updated_at = summary_node.created_at
summary_node.content = summary.encode("utf-8")

# Store the summary node in the database
db.set_node(summary_node.uuid, summary_node.SerializeToString())

# Add an edge from the summary node to the root node
db.add_edge(summary_node.uuid, root_uuid, "summarises", "out")
db.add_edge(root_uuid, summary_node.uuid, "summarises", "in")
```

## Background Processing

The summarisation is performed as a background task to avoid blocking the API:

```python
@router.post("/", response_model=Dict[str, Any])
async def summarise(
    request: Dict[str, Any],
    background_tasks: BackgroundTasks,
    db: ValkeyClient = Depends(get_db_client),
    ollama_client: OllamaClient = Depends(get_ollama_client),
):
    # Extract request parameters
    root_uuid = request.get("root_uuid")

    # Check if the root node exists
    root_node_data = db.get_node(root_uuid)

    # Add the summarisation task to the background tasks
    background_tasks.add_task(generate_summary, root_uuid, db, ollama_client)

    # Return the status
    return {
        "status": "ok",
        "message": f"Summarisation for node {root_uuid} started",
    }
```

## Error Handling

The worker handles errors gracefully and logs them for debugging:

```python
try:
    # Summarisation logic
except Exception as e:
    print(f"Error generating summary: {e}")
    return None
```

## Future Enhancements

- Implement a more sophisticated text chunking algorithm
- Add support for different summarisation models
- Implement a caching layer for frequently requested summaries
- Add support for incremental summarisation of new interactions

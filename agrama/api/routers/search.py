"""
Search router for Agrama API
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List, Optional, Any

from agrama.db import ValkeyClient
from agrama.vector import FaissClient
from agrama.proto.generated.node_pb2 import Node

router = APIRouter()


def get_db_client():
    """Get a database client."""
    return ValkeyClient()


def get_vector_client():
    """Get a vector client."""
    return FaissClient()


@router.post("/semantic_search", response_model=List[Dict[str, Any]])
async def semantic_search(
    request: Dict[str, Any],
    db: ValkeyClient = Depends(get_db_client),
    vector_client: FaissClient = Depends(get_vector_client),
):
    """Search for nodes by vector similarity.

    Args:
        request: The search request.
        db: The database client.
        vector_client: The vector client.

    Returns:
        The search results.
    """
    try:
        # Extract search parameters
        embedding = request.get("embedding", [])
        k = request.get("k", 10)
        query = request.get("query", "")

        # If embedding is missing, fall back to keyword search
        if not embedding:
            if not query:
                raise HTTPException(
                    status_code=400, detail="Missing required field: embedding or query"
                )

            # Fall back to keyword search
            return await keyword_search(
                q=query, k=k, fields=request.get("fields"), db=db
            )

        # Search for similar vectors
        vec_ids, distances = vector_client.search(embedding, k)

        # Map vector IDs to node UUIDs
        uuids = db.get_vector_mappings(vec_ids)

        # Get nodes for each UUID
        results = []
        for i, uuid in enumerate(uuids):
            if uuid:
                # Get the node from the database
                node_data = db.get_node(uuid)

                if node_data:
                    # Parse the node data
                    node = Node()
                    node.ParseFromString(node_data)

                    # Add the node to the results
                    content = node.content.decode("utf-8", errors="ignore")
                    results.append(
                        {
                            "uuid": node.uuid,
                            "type": node.type,
                            "created_at": node.created_at,
                            "updated_at": node.updated_at,
                            "content": content,
                            "distance": float(distances[i]),
                        }
                    )

        # Return the results
        return results
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/keyword_search", response_model=List[Dict[str, Any]])
async def keyword_search(
    q: str,
    k: int = 10,
    fields: Optional[str] = None,
    db: ValkeyClient = Depends(get_db_client),
):
    """Search for nodes by keywords.

    Args:
        q: The search query.
        k: The number of results to return.
        fields: The fields to search in, comma-separated.
        db: The database client.

    Returns:
        The search results.
    """
    try:
        # This is a placeholder for a real keyword search implementation
        # In a real implementation, we would need to use a text search engine
        # like Elasticsearch or implement BM25 search in Valkey

        # For now, we'll just return a dummy result
        return [
            {
                "uuid": "dummy-uuid",
                "type": "DummyNode",
                "created_at": 0,
                "updated_at": 0,
                "content": f"Dummy result for query: {q}",
                "score": 1.0,
            }
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

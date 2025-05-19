"""
Edges router for Agrama API
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Dict, List, Optional, Any

from agrama.db import ValkeyClient

router = APIRouter()


def get_db_client():
    """Get a database client."""
    return ValkeyClient()


@router.put("/", response_model=Dict[str, Any])
async def create_edge(edge: Dict[str, Any], db: ValkeyClient = Depends(get_db_client)):
    """Create an edge between two nodes.

    Args:
        edge: The edge data.
        db: The database client.

    Returns:
        The created edge.
    """
    try:
        # Extract edge data
        src = edge.get("src")
        dst = edge.get("dst")
        edge_type = edge.get("type")

        if not src or not dst or not edge_type:
            raise HTTPException(
                status_code=400, detail="Missing required fields: src, dst, type"
            )

        # Add the edge in both directions
        db.add_edge(src, dst, edge_type, "out")
        db.add_edge(dst, src, edge_type, "in")

        # Return the edge data
        return {
            "src": src,
            "dst": dst,
            "type": edge_type,
            "weight": edge.get("weight", 1.0),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{src}", response_model=Dict[str, List[Dict[str, Any]]])
async def get_edges(
    src: str,
    edge_type: Optional[str] = None,
    direction: str = Query("out", regex="^(out|in)$"),
    db: ValkeyClient = Depends(get_db_client),
):
    """Get edges for a node.

    Args:
        src: The source node UUID.
        edge_type: The type of the edge.
        direction: The direction of the edge, either "out" or "in".
        db: The database client.

    Returns:
        The edges for the node.
    """
    try:
        # Get all edge types if not specified
        if not edge_type:
            # This is a placeholder - in a real implementation, we would need to
            # query all edge types for the node, which would require additional
            # metadata storage in the database
            edge_types = ["contains", "references", "follows", "summarizes"]
        else:
            edge_types = [edge_type]

        # Get edges for each type
        edges = []
        for et in edge_types:
            targets = db.get_edges(src, et, direction)
            for target in targets:
                edges.append(
                    {
                        "src": src if direction == "out" else target,
                        "dst": target if direction == "out" else src,
                        "type": et,
                        "weight": 1.0,  # Default weight
                    }
                )

        # Return the edges
        return {"edges": edges}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

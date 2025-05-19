"""
Nodes router for Agrama API
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any
import uuid
import time

from agrama.db import ValkeyClient
from agrama.proto.generated.node_pb2 import Node

router = APIRouter()


def get_db_client():
    """Get a database client."""
    return ValkeyClient()


@router.put("/", response_model=Dict[str, Any])
async def create_or_update_node(
    request: Dict[str, Any], db: ValkeyClient = Depends(get_db_client)
):
    """Create or update a node.

    Args:
        request: The node data.
        db: The database client.

    Returns:
        The created or updated node.
    """
    try:
        # Create a new node
        node = Node()

        # Set UUID if provided, otherwise generate a new one
        node.uuid = request.get("uuid", str(uuid.uuid4()))

        # Set other fields
        node.type = request.get("type", "")
        node.created_at = request.get("created_at", int(time.time() * 1000))
        node.updated_at = int(time.time() * 1000)

        # Set content if provided
        content = request.get("content", "")
        if isinstance(content, str):
            node.content = content.encode("utf-8")
        elif isinstance(content, bytes):
            node.content = content

        # Set embedding if provided
        embedding = request.get("embedding", [])
        if embedding:
            node.embedding.extend(embedding)

        # Store the node in the database
        db.set_node(node.uuid, node.SerializeToString())

        # Return the node data
        return {
            "uuid": node.uuid,
            "type": node.type,
            "created_at": node.created_at,
            "updated_at": node.updated_at,
            "content": content
            if isinstance(content, str)
            else content.decode("utf-8", errors="ignore"),
            "embedding": list(node.embedding),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{uuid}", response_model=Dict[str, Any])
async def get_node(uuid: str, db: ValkeyClient = Depends(get_db_client)):
    """Get a node by UUID.

    Args:
        uuid: The UUID of the node.
        db: The database client.

    Returns:
        The node data.
    """
    try:
        # Get the node from the database
        node_data = db.get_node(uuid)

        if not node_data:
            raise HTTPException(
                status_code=404, detail=f"Node with UUID {uuid} not found"
            )

        # Parse the node data
        node = Node()
        node.ParseFromString(node_data)

        # Return the node data
        return {
            "uuid": node.uuid,
            "type": node.type,
            "created_at": node.created_at,
            "updated_at": node.updated_at,
            "content": node.content.decode("utf-8", errors="ignore"),
            "embedding": list(node.embedding),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{uuid}/at/{ts}", response_model=Dict[str, Any])
async def get_node_at_time(
    uuid: str, ts: int, db: ValkeyClient = Depends(get_db_client)
):
    """Get a node by UUID at a specific time.

    Args:
        uuid: The UUID of the node.
        ts: The timestamp in milliseconds.
        db: The database client.

    Returns:
        The node data at the specified time.
    """
    try:
        # Get the node from the database at the specified time
        node_data = db.get_node_at_time(uuid, ts)

        if not node_data:
            raise HTTPException(
                status_code=404, detail=f"Node with UUID {uuid} at time {ts} not found"
            )

        # Parse the node data
        node = Node()
        node.ParseFromString(node_data)

        # Return the node data
        return {
            "uuid": node.uuid,
            "type": node.type,
            "created_at": node.created_at,
            "updated_at": node.updated_at,
            "content": node.content.decode("utf-8", errors="ignore"),
            "embedding": list(node.embedding),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

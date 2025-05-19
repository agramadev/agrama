"""
Summarise router for Agrama API
"""

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from typing import Dict, Any
import uuid
import time

from agrama.db import ValkeyClient
from agrama.summariser import OllamaClient
from agrama.proto.generated.node_pb2 import Node

router = APIRouter()


def get_db_client():
    """Get a database client."""
    return ValkeyClient()


def get_ollama_client():
    """Get an Ollama client."""
    return OllamaClient()


async def gather_interaction_nodes(root_uuid: str, db: ValkeyClient):
    """Gather all Interaction nodes under a root UUID using DFS.

    Args:
        root_uuid: The root UUID.
        db: The database client.

    Returns:
        A list of Interaction nodes.
    """
    # This is a placeholder for a real DFS implementation
    # In a real implementation, we would need to traverse the graph
    # and collect all Interaction nodes

    # For now, we'll just return a dummy list
    return []


async def generate_summary(
    root_uuid: str, db: ValkeyClient, ollama_client: OllamaClient
):
    """Generate a summary for a subgraph.

    Args:
        root_uuid: The root UUID.
        db: The database client.
        ollama_client: The Ollama client.
    """
    try:
        # Gather all Interaction nodes under the root UUID
        interaction_nodes = await gather_interaction_nodes(root_uuid, db)

        # Extract text from each node
        texts = []
        for node_data in interaction_nodes:
            node = Node()
            node.ParseFromString(node_data)
            texts.append(node.content.decode("utf-8", errors="ignore"))

        # Join the texts
        text = "\n\n".join(texts)

        # Generate a summary
        summary = await ollama_client.summarise(text)

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

        return summary_node.uuid
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None


@router.post("/", response_model=Dict[str, Any])
async def summarise(
    request: Dict[str, Any],
    background_tasks: BackgroundTasks,
    db: ValkeyClient = Depends(get_db_client),
    ollama_client: OllamaClient = Depends(get_ollama_client),
):
    """Generate a summary for a subgraph.

    Args:
        request: The summarise request.
        background_tasks: The background tasks.
        db: The database client.
        ollama_client: The Ollama client.

    Returns:
        The status of the summarisation request.
    """
    try:
        # Extract request parameters
        root_uuid = request.get("root_uuid")

        if not root_uuid:
            raise HTTPException(
                status_code=400, detail="Missing required field: root_uuid"
            )

        # Check if the root node exists
        root_node_data = db.get_node(root_uuid)

        if not root_node_data:
            raise HTTPException(
                status_code=404, detail=f"Node with UUID {root_uuid} not found"
            )

        # Add the summarisation task to the background tasks
        background_tasks.add_task(generate_summary, root_uuid, db, ollama_client)

        # Return the status
        return {
            "status": "ok",
            "message": f"Summarisation for node {root_uuid} started",
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

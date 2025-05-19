"""
MCP proxy router for Agrama API
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from agrama.db import ValkeyClient

router = APIRouter()


def get_db_client():
    """Get a database client."""
    return ValkeyClient()


@router.get("/tools", response_model=Dict[str, Any])
async def get_tools():
    """Get available tools.

    Returns:
        The available tools.
    """
    try:
        # Return the available tools in MCP format
        return {
            "tools": [
                {
                    "name": "agrama_search",
                    "description": "Search for nodes in the Agrama knowledge graph",
                    "input_schema": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query",
                            },
                            "k": {
                                "type": "integer",
                                "description": "The number of results to return",
                                "default": 10,
                            },
                        },
                        "required": ["query"],
                    },
                },
                {
                    "name": "agrama_summarise",
                    "description": "Generate a summary for a subgraph",
                    "input_schema": {
                        "type": "object",
                        "properties": {
                            "root_uuid": {
                                "type": "string",
                                "description": "The root UUID of the subgraph",
                            }
                        },
                        "required": ["root_uuid"],
                    },
                },
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tools/{tool_name}", response_model=Dict[str, Any])
async def call_tool(tool_name: str, request: Dict[str, Any]):
    """Call a tool.

    Args:
        tool_name: The name of the tool.
        request: The tool request.

    Returns:
        The tool response.
    """
    try:
        if tool_name == "agrama_search":
            # Translate to AAP semantic search
            query = request.get("query")
            request.get("k", 10)

            # This is a placeholder - in a real implementation, we would
            # generate an embedding for the query and call the semantic search endpoint

            # For now, we'll just return a dummy result
            return {
                "results": [
                    {
                        "uuid": "dummy-uuid",
                        "type": "DummyNode",
                        "content": f"Dummy result for query: {query}",
                        "score": 1.0,
                    }
                ]
            }
        elif tool_name == "agrama_summarise":
            # Translate to AAP summarise
            root_uuid = request.get("root_uuid")

            if not root_uuid:
                raise HTTPException(
                    status_code=400, detail="Missing required field: root_uuid"
                )

            # This is a placeholder - in a real implementation, we would
            # call the summarise endpoint

            # For now, we'll just return a dummy result
            return {"summary": f"Dummy summary for root UUID: {root_uuid}"}
        else:
            raise HTTPException(status_code=404, detail=f"Tool {tool_name} not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/resources", response_model=Dict[str, Any])
async def get_resources():
    """Get available resources.

    Returns:
        The available resources.
    """
    try:
        # Return the available resources in MCP format
        return {"resources": []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prompts", response_model=Dict[str, Any])
async def get_prompts():
    """Get available prompts.

    Returns:
        The available prompts.
    """
    try:
        # Return the available prompts in MCP format
        return {"prompts": []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
Key schema conventions for Agrama
"""

import uuid
from typing import Tuple, Optional


def new_uuid() -> str:
    """Generate a new UUID.

    Returns:
        A new UUID as a string.
    """
    return str(uuid.uuid4())


def make_node_key(uuid_str: str, node_type: Optional[str] = None) -> str:
    """Make a key for a node.

    Args:
        uuid_str: The UUID of the node.
        node_type: The type of the node (not used in the key).

    Returns:
        The key for the node.
    """
    return f"mem:{uuid_str}"


def parse_node_key(key: str) -> Tuple[str, Optional[str]]:
    """Parse a node key.

    Args:
        key: The key to parse.

    Returns:
        A tuple of (uuid, node_type).
    """
    # Check if the key is a node key
    if not key.startswith("mem:"):
        raise ValueError(f"Invalid node key: {key}")

    # Extract the UUID
    uuid_str = key[4:]

    # Return the UUID and node type (None since it's not stored in the key)
    return uuid_str, None


def make_edge_key(uuid_str: str, edge_type: str, direction: str) -> str:
    """Make a key for an edge.

    Args:
        uuid_str: The UUID of the node.
        edge_type: The type of the edge.
        direction: The direction of the edge, either "out" or "in".

    Returns:
        The key for the edge.
    """
    if direction not in ["out", "in"]:
        raise ValueError("Direction must be either 'out' or 'in'")

    return f"mem:{uuid_str}:{direction}:{edge_type}"


def parse_edge_key(key: str) -> Tuple[str, str, str]:
    """Parse an edge key.

    Args:
        key: The key to parse.

    Returns:
        A tuple of (uuid, direction, edge_type).
    """
    # Check if the key is an edge key
    if not key.startswith("mem:"):
        raise ValueError(f"Invalid edge key: {key}")

    # Split the key
    parts = key.split(":")

    if len(parts) != 4:
        raise ValueError(f"Invalid edge key: {key}")

    # Extract the UUID, direction, and edge type
    uuid_str = parts[1]
    direction = parts[2]
    edge_type = parts[3]

    # Check the direction
    if direction not in ["out", "in"]:
        raise ValueError(f"Invalid direction: {direction}")

    return uuid_str, direction, edge_type


def make_temporal_key(uuid_str: str, timestamp: int) -> str:
    """Make a key for a temporal node.

    Args:
        uuid_str: The UUID of the node.
        timestamp: The timestamp in milliseconds.

    Returns:
        The key for the temporal node.
    """
    return f"mem:{uuid_str}:ts:{timestamp}"


def parse_temporal_key(key: str) -> Tuple[str, int]:
    """Parse a temporal key.

    Args:
        key: The key to parse.

    Returns:
        A tuple of (uuid, timestamp).
    """
    # Check if the key is a temporal key
    if not key.startswith("mem:"):
        raise ValueError(f"Invalid temporal key: {key}")

    # Split the key
    parts = key.split(":")

    if len(parts) != 4 or parts[2] != "ts":
        raise ValueError(f"Invalid temporal key: {key}")

    # Extract the UUID and timestamp
    uuid_str = parts[1]
    timestamp = int(parts[3])

    return uuid_str, timestamp


def make_vector_key(vec_id: int) -> str:
    """Make a key for a vector mapping.

    Args:
        vec_id: The vector ID.

    Returns:
        The key for the vector mapping.
    """
    return f"vec:{vec_id}"


def parse_vector_key(key: str) -> int:
    """Parse a vector key.

    Args:
        key: The key to parse.

    Returns:
        The vector ID.
    """
    # Check if the key is a vector key
    if not key.startswith("vec:"):
        raise ValueError(f"Invalid vector key: {key}")

    # Extract the vector ID
    vec_id = int(key[4:])

    return vec_id

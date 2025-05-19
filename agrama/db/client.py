"""
Valkey client wrapper for Agrama
"""

import os
from typing import List, Optional
from valkey_glide.client import Redis
from valkey_glide.connection_pool import ConnectionPool


class ValkeyClient:
    """Valkey client wrapper with connection pooling."""

    def __init__(self, url: Optional[str] = None):
        """Initialize the Valkey client.

        Args:
            url: The Valkey URL. If not provided, uses the VALKEY_URL env var.
        """
        default_url = "redis://localhost:6379"
        self.url = url or os.environ.get("VALKEY_URL", default_url)
        self.pool = ConnectionPool.from_url(self.url)
        self.client = Redis(connection_pool=self.pool)

    def ping(self) -> bool:
        """Ping the Valkey server.

        Returns:
            True if the server responds with PONG, False otherwise.
        """
        try:
            return self.client.ping()
        except Exception:
            return False

    def get_node(self, uuid: str) -> Optional[bytes]:
        """Get a node by UUID.

        Args:
            uuid: The UUID of the node.

        Returns:
            The node data as bytes, or None if not found.
        """
        from agrama.db.schema import make_node_key

        key = make_node_key(uuid)
        return self.client.get(key)

    def set_node(
        self, uuid: str, data: bytes, store_history: bool = True
    ) -> bool:
        """Set a node by UUID.

        Args:
            uuid: The UUID of the node.
            data: The node data as bytes.
            store_history: Whether to store the node in the history.

        Returns:
            True if successful, False otherwise.
        """
        from agrama.db.schema import make_node_key, make_temporal_key
        import time

        # Set the node
        key = make_node_key(uuid)
        result = self.client.set(key, data)

        # Store the node in the history if requested
        if store_history and result:
            timestamp = int(time.time() * 1000)
            temporal_key = make_temporal_key(uuid, timestamp)
            self.client.set(temporal_key, data)

            # Set TTL for temporal data (60 days)
            self.client.expire(temporal_key, 60 * 24 * 60 * 60)

        return result

    def get_node_at_time(self, uuid: str, timestamp: int) -> Optional[bytes]:
        """Get a node by UUID at a specific time.

        Args:
            uuid: The UUID of the node.
            timestamp: The timestamp in milliseconds.

        Returns:
            The node data as bytes, or None if not found.
        """
        from agrama.db.schema import make_temporal_key

        key = make_temporal_key(uuid, timestamp)
        return self.client.get(key)

    def add_edge(
        self, src: str, dst: str, edge_type: str, direction: str = "out"
    ) -> bool:
        """Add an edge between two nodes.

        Args:
            src: The source node UUID.
            dst: The destination node UUID.
            edge_type: The type of the edge.
            direction: The direction of the edge, either "out" or "in".

        Returns:
            True if successful, False otherwise.
        """
        from agrama.db.schema import make_edge_key

        key = make_edge_key(src, edge_type, direction)
        return bool(self.client.rpush(key, dst))

    def add_edges_batch(
        self, edges: List[tuple], bidirectional: bool = True
    ) -> bool:
        """Add multiple edges in a batch.

        Args:
            edges: A list of (src, dst, edge_type) tuples.
            bidirectional: Whether to add edges in both directions.

        Returns:
            True if all edges were added successfully, False otherwise.
        """
        from agrama.db.schema import make_edge_key

        # Create a pipeline
        pipeline = self.client.pipeline()

        # Add each edge to the pipeline
        for src, dst, edge_type in edges:
            # Add outgoing edge
            out_key = make_edge_key(src, edge_type, "out")
            pipeline.rpush(out_key, dst)

            # Add incoming edge if bidirectional
            if bidirectional:
                in_key = make_edge_key(dst, edge_type, "in")
                pipeline.rpush(in_key, src)

        # Execute the pipeline
        results = pipeline.execute()

        # Check if all operations were successful
        return all(result > 0 for result in results)

    def get_edges(
        self, uuid: str, edge_type: str, direction: str = "out"
    ) -> List[str]:
        """Get edges for a node.

        Args:
            uuid: The UUID of the node.
            edge_type: The type of the edge.
            direction: The direction of the edge, either "out" or "in".

        Returns:
            A list of node UUIDs.
        """
        from agrama.db.schema import make_edge_key

        key = make_edge_key(uuid, edge_type, direction)
        result = self.client.lrange(key, 0, -1)
        return [item.decode("utf-8") for item in result]

    def set_vector_mapping(self, vec_id: int, uuid: str) -> bool:
        """Set a mapping from vector ID to node UUID.

        Args:
            vec_id: The vector ID.
            uuid: The node UUID.

        Returns:
            True if successful, False otherwise.
        """
        from agrama.db.schema import make_vector_key

        key = make_vector_key(vec_id)
        return self.client.set(key, uuid)

    def get_vector_mapping(self, vec_id: int) -> Optional[str]:
        """Get a mapping from vector ID to node UUID.

        Args:
            vec_id: The vector ID.

        Returns:
            The node UUID, or None if not found.
        """
        from agrama.db.schema import make_vector_key

        key = make_vector_key(vec_id)
        result = self.client.get(key)
        return result.decode("utf-8") if result else None

    def get_vector_mappings(self, vec_ids: List[int]) -> List[Optional[str]]:
        """Get mappings from vector IDs to node UUIDs.

        Args:
            vec_ids: The vector IDs.

        Returns:
            A list of node UUIDs, or None for each ID not found.
        """
        from agrama.db.schema import make_vector_key

        keys = [make_vector_key(vec_id) for vec_id in vec_ids]
        results = self.client.mget(keys)
        return [
            result.decode("utf-8") if result else None for result in results
        ]

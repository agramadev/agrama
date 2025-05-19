#!/usr/bin/env python3
"""
Seed script for Agrama - Loads sample data into the database
"""

import uuid
import time
import random
import numpy as np
from typing import List, Optional
import argparse

from agrama.db import ValkeyClient
from agrama.vector import FaissClient
from agrama.proto.generated.node_pb2 import Node


def generate_random_embedding(dimension: int = 1024) -> List[float]:
    """Generate a random embedding vector.

    Args:
        dimension: The dimension of the vector.

    Returns:
        A random embedding vector.
    """
    # Generate a random vector
    embedding = np.random.randn(dimension).astype(np.float32)

    # Normalize to unit length for cosine similarity
    embedding = embedding / np.linalg.norm(embedding)

    return embedding.tolist()


def create_sample_node(
    node_type: str, content: bytes, embedding: Optional[List[float]] = None
) -> Node:
    """Create a sample node.

    Args:
        node_type: The type of the node.
        content: The content of the node.
        embedding: The embedding vector of the node.

    Returns:
        A sample node.
    """
    node = Node()
    node.uuid = str(uuid.uuid4())
    node.type = node_type
    node.created_at = int(time.time() * 1000)
    node.updated_at = node.created_at
    node.content = content

    if embedding:
        node.embedding.extend(embedding)

    return node


def seed_database(num_nodes: int = 100, dimension: int = 1024) -> None:
    """Seed the database with sample data.

    Args:
        num_nodes: The number of nodes to create.
        dimension: The dimension of the embedding vectors.
    """
    # Initialize clients
    db_client = ValkeyClient()
    vector_client = FaissClient(dimension=dimension)

    # Check if the database is available
    if not db_client.ping():
        print("Error: Could not connect to the database.")
        return

    # Node types
    node_types = ["Session", "Task", "CodeUnit", "Interaction", "Summary"]

    # Create nodes
    nodes = []
    for i in range(num_nodes):
        # Select a random node type
        node_type = random.choice(node_types)

        # Create sample content
        content = f"Sample content for {node_type} {i}".encode("utf-8")

        # Generate a random embedding
        embedding = generate_random_embedding(dimension)

        # Create the node
        node = create_sample_node(node_type, content, embedding)
        nodes.append(node)

        # Store the node in the database
        db_client.set_node(node.uuid, node.SerializeToString())

        # Add the embedding to the vector index
        vec_id = vector_client.add(embedding)

        # Store the mapping from vector ID to node UUID
        db_client.set_vector_mapping(vec_id, node.uuid)

        # Print progress
        if (i + 1) % 10 == 0:
            print(f"Created {i + 1} nodes...")

    # Create edges between nodes
    num_edges = min(num_nodes * 2, num_nodes * (num_nodes - 1))
    for _ in range(num_edges):
        # Select random source and destination nodes
        src_node = random.choice(nodes)
        dst_node = random.choice(nodes)

        # Skip self-edges
        if src_node.uuid == dst_node.uuid:
            continue

        # Select a random edge type
        edge_types = ["contains", "references", "follows", "summarizes"]
        edge_type = random.choice(edge_types)

        # Add the edge
        db_client.add_edge(src_node.uuid, dst_node.uuid, edge_type, "out")
        db_client.add_edge(dst_node.uuid, src_node.uuid, edge_type, "in")

    print(f"Created {num_nodes} nodes and {num_edges} edges.")


def main() -> None:
    """Main entry point for the seed script."""
    parser = argparse.ArgumentParser(
        description="Seed the Agrama database with sample data."
    )
    parser.add_argument(
        "--num-nodes", type=int, default=100, help="Number of nodes to create"
    )
    parser.add_argument(
        "--dimension", type=int, default=1024, help="Dimension of embedding vectors"
    )

    args = parser.parse_args()

    print(f"Seeding database with {args.num_nodes} nodes...")
    seed_database(args.num_nodes, args.dimension)
    print("Done!")


if __name__ == "__main__":
    main()

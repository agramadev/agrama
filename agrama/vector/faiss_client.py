"""
Faiss wrapper for vector search
"""

import os
import uuid
import numpy as np
from typing import List, Tuple, Optional
import faiss


class FaissClient:
    """Faiss client wrapper for vector search."""

    def __init__(self, dimension: int = 1024, host: Optional[str] = None):
        """Initialize the Faiss client.

        Args:
            dimension: The dimension of the vectors.
            host: The Faiss host. If not provided, uses the FAISS_HOST environment variable.
        """
        self.dimension = dimension
        self.host = host or os.environ.get("FAISS_HOST", "localhost")
        self.index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        self.index_id_map = faiss.IndexIDMap(self.index)

    def add(self, embedding: List[float], vec_id: Optional[int] = None) -> int:
        """Add a vector to the index.

        Args:
            embedding: The vector to add.
            vec_id: The ID to assign to the vector. If not provided, a random ID is generated.

        Returns:
            The ID assigned to the vector.
        """
        if vec_id is None:
            # Generate a 64-bit ID from a UUID
            vec_id = int(uuid.uuid4().int >> 64)

        # Convert the embedding to a numpy array
        embedding_np = np.array([embedding], dtype=np.float32)

        # Add the vector to the index
        self.index_id_map.add_with_ids(embedding_np, np.array([vec_id], dtype=np.int64))

        return vec_id

    def search(
        self, embedding: List[float], k: int = 10
    ) -> Tuple[List[int], List[float]]:
        """Search for similar vectors.

        Args:
            embedding: The query vector.
            k: The number of results to return.

        Returns:
            A tuple of (vector IDs, distances).
        """
        # Convert the embedding to a numpy array
        embedding_np = np.array([embedding], dtype=np.float32)

        # Search the index
        distances, indices = self.index_id_map.search(embedding_np, k)

        # Convert to Python lists
        return indices[0].tolist(), distances[0].tolist()

    def remove(self, vec_id: int) -> bool:
        """Remove a vector from the index.

        Args:
            vec_id: The ID of the vector to remove.

        Returns:
            True if successful, False otherwise.
        """
        try:
            self.index_id_map.remove_ids(np.array([vec_id], dtype=np.int64))
            return True
        except Exception:
            return False

    def reset(self) -> None:
        """Reset the index."""
        self.index = faiss.IndexFlatIP(self.dimension)
        self.index_id_map = faiss.IndexIDMap(self.index)

    def save(self, path: str) -> bool:
        """Save the index to a file.

        Args:
            path: The path to save the index to.

        Returns:
            True if successful, False otherwise.
        """
        try:
            faiss.write_index(self.index_id_map, path)
            return True
        except Exception:
            return False

    def load(self, path: str) -> bool:
        """Load the index from a file.

        Args:
            path: The path to load the index from.

        Returns:
            True if successful, False otherwise.
        """
        try:
            self.index_id_map = faiss.read_index(path)
            self.index = self.index_id_map.index
            return True
        except Exception:
            return False

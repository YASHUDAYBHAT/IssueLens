import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int = 384):
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embedding, chunk):
        vector = np.array([embedding], dtype="float32")

        self.index.add(vector)
        self.chunks.append(chunk)

    def search(self, embedding, k=5):
        vector = np.array([embedding], dtype="float32")

        scores, indices = self.index.search(vector, k)

        results = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            results.append(
                (
                    float(score),
                    self.chunks[idx],
                )
            )

        return results


vector_store = VectorStore()
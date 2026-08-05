import faiss
import numpy as np


class IssueVectorStore:

    def __init__(self):
        self.index = faiss.IndexFlatIP(384)
        self.issues = []

    def add(self, embedding, issue):

        vector = np.array(
            [embedding],
            dtype="float32",
        )

        faiss.normalize_L2(vector)

        self.index.add(vector)

        self.issues.append(issue)

    def search(
        self,
        embedding,
        k=5,
    ):

        vector = np.array(
            [embedding],
            dtype="float32",
        )

        faiss.normalize_L2(vector)

        scores, indices = self.index.search(
            vector,
            k,
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0],
        ):

            if idx == -1:
                continue

            results.append(
                (
                    float(score),
                    self.issues[idx],
                )
            )

        return results

    def clear(self):

        self.index = faiss.IndexFlatIP(384)

        self.issues = []


issue_vector_store = IssueVectorStore()
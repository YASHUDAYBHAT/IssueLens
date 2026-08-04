from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, text: str):
        return self.model.encode(
            text,
            normalize_embeddings=True,
        )


embedder = Embedder()
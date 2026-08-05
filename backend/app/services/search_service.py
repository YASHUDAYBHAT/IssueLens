from app.indexing.embedder import embedder
from app.indexing.vector_store import vector_store


class SearchService:

    def search(
        self,
        query: str,
        k: int = 5,
    ):

        embedding = embedder.embed(query)

        return vector_store.search(
            embedding,
            k,
        )


search_service = SearchService()
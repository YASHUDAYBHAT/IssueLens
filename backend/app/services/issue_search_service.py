from app.indexing.embedder import embedder
from app.indexing.issue_vector_store import issue_vector_store


class IssueSearchService:

    def search(self, query: str, k: int = 5):

        embedding = embedder.embed(query)

        return issue_vector_store.search(
            embedding,
            k,
        )


issue_search_service = IssueSearchService()
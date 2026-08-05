from app.indexing.embedder import embedder
from app.indexing.issue_vector_store import issue_vector_store


class IssueIndexService:

    def index(self, issues):

        issue_vector_store.clear()
        count = 0

        for issue in issues:

            text = (
                issue["title"]
                + "\n\n"
                + (issue.get("body") or "")
            )

            embedding = embedder.embed(text)

            issue_vector_store.add(
                embedding,
                issue,
            )

            count += 1

        return count


issue_index_service = IssueIndexService()
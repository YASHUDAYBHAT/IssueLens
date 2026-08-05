from app.db.database import db


class IssueRepository:

    async def create_many(
        self,
        issues,
    ):

        if not issues:
            return

        await db.issues.insert_many(
            issues
        )

    async def find_by_repository(
        self,
        repository: str,
    ):

        cursor = db.issues.find(
            {
                "repository": repository
            }
        )

        return await cursor.to_list(None)


issue_repository = IssueRepository()
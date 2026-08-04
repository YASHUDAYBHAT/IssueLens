from app.db.database import db


class RepositoryRepository:

    async def create(self, data: dict):

        result = await db.repositories.insert_one(data)

        return str(result.inserted_id)


repository_repository = RepositoryRepository()
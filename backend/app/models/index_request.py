from pydantic import BaseModel


class RepositoryIndexRequest(BaseModel):
    repository: str
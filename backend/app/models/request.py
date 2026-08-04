from pydantic import BaseModel


class RepositoryImportRequest(BaseModel):
    repository: str
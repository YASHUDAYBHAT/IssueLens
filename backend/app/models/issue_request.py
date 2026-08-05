from pydantic import BaseModel


class IssueImportRequest(BaseModel):

    repository: str
from pydantic import BaseModel


class IssueIndexRequest(BaseModel):

    repository: str
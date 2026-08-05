from pydantic import BaseModel


class IssueSearchRequest(BaseModel):

    query: str

    k: int = 5
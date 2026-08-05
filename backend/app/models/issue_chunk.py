from pydantic import BaseModel


class IssueChunk(BaseModel):
    repository: str
    github_id: int
    issue_number: int
    title: str
    body: str | None = None
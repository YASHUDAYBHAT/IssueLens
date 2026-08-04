from pydantic import BaseModel


class Repository(BaseModel):
    github_id: int
    owner: str
    name: str
    full_name: str
    description: str | None = None
    stars: int
    forks: int
    open_issues: int
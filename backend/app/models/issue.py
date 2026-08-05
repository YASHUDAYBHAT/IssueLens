from pydantic import BaseModel


class Issue(BaseModel):

    github_id: int

    repository: str

    number: int

    title: str

    body: str | None = None

    state: str

    url: str
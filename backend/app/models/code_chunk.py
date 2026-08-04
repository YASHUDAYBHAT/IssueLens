from pydantic import BaseModel


class CodeChunk(BaseModel):
    repository: str

    qualified_name: str

    kind: str

    language: str

    file_path: str

    source_code: str

    docstring: str | None = None

    start_line: int

    end_line: int
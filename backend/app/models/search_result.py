from pydantic import BaseModel


class SearchResult(BaseModel):
    score: float
    qualified_name: str
    file_path: str
    start_line: int
    end_line: int
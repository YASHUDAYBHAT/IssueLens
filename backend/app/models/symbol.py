from pydantic import BaseModel


class Symbol(BaseModel):

    qualified_name: str

    kind: str

    file_path: str

    start_line: int

    end_line: int
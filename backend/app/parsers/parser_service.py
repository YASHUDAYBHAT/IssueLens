from pathlib import Path

from app.parsers.python_parser import python_parser

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "docs",
    "tests",
    "examples",
}


class ParserService:

    def parse_repository(self, repository_path: str):

        repository = Path(repository_path)

        symbols = []

        for file in repository.rglob("*.py"):

            print(file)   # <-- DEBUG

            if any(part in IGNORE_DIRS for part in file.parts):
                print("Skipped")
                continue

            print("Parsing")

            try:
                symbols.extend(
                    python_parser.parse_file(file)
                )

            except Exception as e:
                print(e)

        return symbols


parser_service = ParserService()
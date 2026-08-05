from pathlib import Path

from app.indexing.chunker import python_chunker
from app.indexing.embedder import embedder
from app.indexing.utils import chunk_to_text
from app.indexing.vector_store import vector_store


class IndexService:

    def index_repository(
        self,
        repository: str,
        repository_path: str,
    ):

        repository_path = Path(repository_path)

        total_chunks = 0

        for file in repository_path.rglob("*.py"):

            if any(
                part in {
                    ".git",
                    ".venv",
                    "__pycache__",
                    "tests",
                    "docs",
                    "examples",
                }
                for part in file.parts
            ):
                continue

            chunks = python_chunker.chunk_file(
                repository,
                file,
            )

            for chunk in chunks:

                text = chunk_to_text(chunk)

                embedding = embedder.embed(text)

                vector_store.add(
                    embedding,
                    chunk,
                )

                total_chunks += 1

        return total_chunks


index_service = IndexService()
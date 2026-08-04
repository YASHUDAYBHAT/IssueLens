from app.models.code_chunk import CodeChunk


def chunk_to_text(chunk: CodeChunk) -> str:
    """
    Convert a CodeChunk into text for embedding.
    """

    parts = [
        f"Qualified Name: {chunk.qualified_name}",
        f"Kind: {chunk.kind}",
    ]

    if chunk.docstring:
        parts.append(f"Docstring:\n{chunk.docstring}")

    parts.append(f"Source Code:\n{chunk.source_code}")

    return "\n\n".join(parts)
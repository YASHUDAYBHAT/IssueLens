import ast
from pathlib import Path

from app.models.code_chunk import CodeChunk


class PythonChunker:

    def chunk_file(self, repository: str, file_path: Path):

        source = file_path.read_text(encoding="utf-8")
        lines = source.splitlines()
        tree = ast.parse(source)

        chunks = []

        class_stack = []

        class Visitor(ast.NodeVisitor):

            def visit_ClassDef(self, node):

                class_stack.append(node.name)

                chunk = "\n".join(
                    lines[node.lineno - 1 : node.end_lineno]
                )

                chunks.append(
                    CodeChunk(
                        repository=repository,
                        qualified_name=".".join(class_stack),
                        kind="class",
                        language="python",
                        file_path=str(file_path),
                        source_code=chunk,
                        docstring=ast.get_docstring(node),
                        start_line=node.lineno,
                        end_line=node.end_lineno,
                    )
                )

                self.generic_visit(node)
                class_stack.pop()

            def visit_FunctionDef(self, node):

                if class_stack:
                    qualified = ".".join(class_stack + [node.name])
                    kind = "method"
                else:
                    qualified = node.name
                    kind = "function"

                chunk = "\n".join(
                    lines[node.lineno - 1 : node.end_lineno]
                )

                chunks.append(
                    CodeChunk(
                        repository=repository,
                        qualified_name=qualified,
                        kind=kind,
                        language="python",
                        file_path=str(file_path),
                        source_code=chunk,
                        docstring=ast.get_docstring(node),
                        start_line=node.lineno,
                        end_line=node.end_lineno,
                    )
                )

                self.generic_visit(node)

        Visitor().visit(tree)

        return chunks


python_chunker = PythonChunker()
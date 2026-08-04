import ast
from pathlib import Path

from app.models.symbol import Symbol


class SymbolVisitor(ast.NodeVisitor):

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.class_stack = []
        self.symbols = []

    def visit_ClassDef(self, node: ast.ClassDef):
        qualified = ".".join(self.class_stack + [node.name])

        self.symbols.append(
            Symbol(
                qualified_name=qualified,
                kind="class",
                file_path=str(self.file_path),
                start_line=node.lineno,
                end_line=node.end_lineno,
            )
        )

        self.class_stack.append(node.name)
        self.generic_visit(node)
        self.class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if self.class_stack:
            qualified = ".".join(self.class_stack + [node.name])
            kind = "method"
        else:
            qualified = node.name
            kind = "function"

        self.symbols.append(
            Symbol(
                qualified_name=qualified,
                kind=kind,
                file_path=str(self.file_path),
                start_line=node.lineno,
                end_line=node.end_lineno,
            )
        )

        self.generic_visit(node)


class PythonParser:

    def parse_file(self, file_path: Path):
        tree = ast.parse(file_path.read_text(encoding="utf-8"))

        visitor = SymbolVisitor(file_path)
        visitor.visit(tree)

        return visitor.symbols


python_parser = PythonParser()
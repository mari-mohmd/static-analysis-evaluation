"""
Simple DivisionByZero static analyzer module
"""

import ast

class DivisionByZeroChecker(ast.NodeVisitor):
    def __init__(self):
        self.env = {}

    def visit_Assign(self, node):
        target = node.targets[0]
        name = target.id
        value = self.visit(node.value)
        self.env[name] = value

    def visit_Constant(self, node):
        return node.value

    def visit_Name(self, node):
        return self.env[node.id]

    def visit_BinOp(self, node):
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type == ast.Div:
            if right == 0:
                print(f"{node.lineno} Error div by zero!!!")

    def visit_Expr(self, node):
        return self.visit(node.value)

# ------------ Main Operation ------------

# Code Example
code = """
y = 1 / 0
"""

tree = ast.parse(code)
ev = DivisionByZeroChecker()
ev.visit(tree)

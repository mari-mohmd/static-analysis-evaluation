"""
Generates a graph demonstrating division by zero.
Prerequisite:
  Install Graphviz: pip install graphviz
Usage:
  python division_by_zero_ast.py
"""
import ast
import graphviz

def gen_ast_graph(code):
    tree = ast.parse(code)
    d = graphviz.Digraph()

    def create_graph_nodes_edges(node, parent_name=None):
        node_id = str(id(node))
        node_label = node.__class__.__name__
        d.node(node_id, node_label)

        if parent_name:
            d.edge(parent_name, node_id)

        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        create_graph_nodes_edges(item, node_id)
            elif isinstance(value, ast.AST):
                create_graph_nodes_edges(value, node_id)

    create_graph_nodes_edges(tree)
    return d

code_to_graph = "x = 1/0"

ast_graph = gen_ast_graph(code_to_graph)
ast_graph.render('division_by_zero_graph', view=True)

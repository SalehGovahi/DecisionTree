import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout


def draw_tree(graph):
    pos = graphviz_layout(graph, prog='dot', root=0)
    labels = {node: graph.nodes[node]['label'] for node in graph.nodes}
    plt.figure(figsize=(10, 10))
    nx.draw(graph, pos, with_labels=False, arrows=False)
    nx.draw_networkx_labels(graph, pos, labels=labels)
    plt.show()


def plot_tree(node, graph=None):
    if graph is None:
        graph = nx.DiGraph()
        graph.add_node(node.id, label=node.feature_name)

    for child in node.children:
        graph.add_edge(node.id, child.id)
        plot_tree(child, graph)

    return graph

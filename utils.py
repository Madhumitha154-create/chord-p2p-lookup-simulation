import networkx as nx
import matplotlib.pyplot as plt

def draw_ring(nodes, highlight_path=None):
    G = nx.Graph()

    for node in nodes:
        G.add_node(node)

    for i in range(len(nodes)):
        G.add_edge(nodes[i], nodes[(i + 1) % len(nodes)])

    pos = nx.circular_layout(G)

    plt.figure(figsize=(6,6))

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800)

    # Highlight lookup path
    if highlight_path:
        edges = list(zip(highlight_path, highlight_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=3)

    return plt
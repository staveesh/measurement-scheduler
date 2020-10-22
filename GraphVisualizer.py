import networkx as nx
import matplotlib.pyplot as plt
from SubGraph import SubGraph
from ConflictGraph import ConflictGraph


class GraphVisualizer:

    def __init__(self, scalefactor=0.05, node_size=15000, alpha=0.5):
        self.scalefactor = scalefactor
        self.node_size = node_size
        self.alpha = alpha

    def visualize(self, graph):
        G = nx.Graph()

        if type(graph) == SubGraph:
            for node in graph.get_nodes():
                G.add_node(node.get_label())
                for neighbor in node.get_neighbors():
                    G.add_edge(node.get_label(), neighbor.get_label())
            nx.draw(G, with_labels=True)

        elif type(graph) == ConflictGraph:
            # lookup table for node and its subgraph
            lookup = {}
            for node in graph.get_nodes():
                H = nx.Graph()
                for subvertex in node.get_subgraph().get_nodes():
                    H.add_node(subvertex.get_label())
                    for neighbor in subvertex.get_neighbors():
                        H.add_edge(subvertex.get_label(), neighbor.get_label())
                lookup[node] = H
            for u, v in graph.get_edges():
                G.add_edge(lookup[u], lookup[v])
                G.add_edge(lookup[v], lookup[u])

            Gpos = nx.spring_layout(G)
            nx.draw_networkx_edges(G, pos=Gpos)
            nx.draw_networkx_nodes(G, pos=Gpos, node_size=self.node_size, alpha=self.alpha)
            for node in G.nodes():
                if type(node) == nx.Graph:
                    Hpos = nx.spring_layout(node)
                    for subnode in node.nodes():
                        Hpos[subnode] = Hpos[subnode] * self.scalefactor + Gpos[node]
                    nx.draw(node, pos=Hpos, with_labels=True)

        plt.show()

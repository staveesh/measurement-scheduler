from SubNode import SubNode
from itertools import combinations


class SubGraph:

    def __init__(self, num_nodes):
        self.nodes = []
        for i in range(num_nodes):
            node = SubNode(i+1)
            self.nodes.append(node)
        for node1, node2 in combinations(self.nodes, 2):
            node1.add_neighbor(node2)
            node2.add_neighbor(node1)

    def get_nodes(self):
        return self.nodes

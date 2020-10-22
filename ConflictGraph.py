class ConflictGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def get_edges(self):
        return self.edges
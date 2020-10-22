class SubNode:
    def __init__(self, label):
        self.neighbors = []
        self.label = label

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_neighbors(self):
        return self.neighbors

    def get_label(self):
        return self.label
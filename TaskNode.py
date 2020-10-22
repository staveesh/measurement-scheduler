from SubGraph import SubGraph

class TaskNode:

    def __init__(self, label, arrival_time, execution_time, period):
        self.neighbors = []
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.period = period
        self.label = label
        self.subgraph = SubGraph(self.execution_time)

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_subgraph(self):
        return self.subgraph

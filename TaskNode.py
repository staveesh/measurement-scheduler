from SubGraph import SubGraph


class TaskNode:

    def __init__(self, label, arrival_time, execution_time, period):
        self.colors = set()
        self.neighbors = []
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.period = period
        self.label = label
        self.subgraph = SubGraph(self.execution_time)
        self.degree = execution_time

    def __repr__(self):
        return 'TaskNode [neighbors = {}, arrival_time = {},' \
               ' execution_time = {}, period = {}, label = {}, degree = {} ]'.format(
            self.neighbors, self.arrival_time, self.execution_time, self.period, self.label,
            self.degree
        )

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_neighbors(self):
        return self.neighbors

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_execution_time(self):
        return self.execution_time

    def get_period(self):
        return self.period

    def get_label(self):
        return self.label

    def get_subgraph(self):
        return self.subgraph

    def get_degree(self):
        return self.degree

    def set_degree(self, degree):
        self.degree = degree

    def get_colors(self):
        return self.colors

    def set_colors(self, colors):
        self.colors = colors
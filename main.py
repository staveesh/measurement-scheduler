from GraphVisualizer import GraphVisualizer
from ConflictGraph import ConflictGraph
from TaskNode import TaskNode


if __name__ == '__main__':
    G = ConflictGraph()
    n = int(input('Enter number of jobs : '))
    label_node_lookup = {}
    for i in range(n):
        label, arrival_time, execution_time, period = map(int, input('Enter label, arrival_time, execution_time, '
                                                                     'period of job {} : '.format(i+1))
            .strip().split())
        node = TaskNode(label, arrival_time, execution_time, period)
        label_node_lookup[label] = node
        G.add_node(node)
    m = int(input('Enter number of conflicts : '))
    for i in range(m):
        u, v = map(int, input('Enter conflict {} : '.format(i+1)).strip().split())
        G.add_edge(label_node_lookup[u], label_node_lookup[v])
    visualizer = GraphVisualizer()
    visualizer.visualize(G)

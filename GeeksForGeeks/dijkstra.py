# IN PROGRESS

import math
from collections import defaultdict

# the node class
class Node:
    def __init__(self, value = ''):
        self.value = value
        self.distance = math.inf

    
class Graph:
    def __init__(self):
        self.edge_weight = {}
        self.graph = defaultdict(list)
        self.nodes = {}
    
    def add_edge(self, start_node, end_node, weight):
        self.graph[start_node].append(end_node)
        self.edge_weight[(start_node.value, end_node.value)] = weight
    
    def generate_node_from_list(self, node_value_list):
        for node_value in node_value_list:
            n = Node(node_value)
            self.nodes[node_value] = n


    def djks(self, start_node_value):
        is_visited = set()
        queue = []

        start_node = self.graph.nodes[start_node_value]
        start_node.distance = 0

        queue.append(start_node)

        while len(queue) > 0:

            current_node = queue.pop(0)

            for neighbour in self.graph[current_node.value]:
                if neighbour.value not in is_visited:
                    is_visited.append(neighbour.value)
                    queue.append(neighbour)
                    current_distance = current_node.distance + self.edge_weight[(current_node.value, neighbour.value)]
                    neighbour.distance = min(neighbour.distance, current_distance)
        


node_value_list = ['A', 'B', 'C', 'D', 'E', 'F']
graph = Graph()
graph.generate_node_from_list(node_value_list)

graph.add_edge(graph.nodes['A'], graph.nodes['B'], 2)
graph.add_edge(graph.nodes['A'], graph.nodes['C'], 4)
graph.add_edge(graph.nodes['B'], graph.nodes['C'], 1)
graph.add_edge(graph.nodes['C'], graph.nodes['E'], 3)
graph.add_edge(graph.nodes['B'], graph.nodes['D'], 7)
graph.add_edge(graph.nodes['C'], graph.nodes['E'], 3)
graph.add_edge(graph.nodes['E'], graph.nodes['D'], 2)
graph.add_edge(graph.nodes['D'], graph.nodes['F'], 1)
graph.add_edge(graph.nodes['E'], graph.nodes['F'], 5)


print(graph.nodes['B'].distance)





    


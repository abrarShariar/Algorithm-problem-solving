from collections import defaultdict

class Graph:

    # constructor
    def __init__(self):
        # making a dictionary with default value set to list for each key
        self.graph = defaultdict(list)

    def addEdge(self, start_node, end_node):
        self.graph[start_node].append(end_node)

    def BFS(self, start_node):
        # initialize a queue
        queue = []
        queue.append(start_node)
        visited = [False] * len(self.graph)

        while len(queue) > 0:
            current_node = queue.pop(0)
            visited[current_node] = True

            print(current_node, end=" ")

            for node in self.graph[current_node]:
                if not visited[node]:
                    queue.append(node)



test_graph = Graph()
test_graph.addEdge(0, 1)
test_graph.addEdge(0, 2)
test_graph.addEdge(1, 2)
test_graph.addEdge(2, 0)
test_graph.addEdge(2, 3)
test_graph.addEdge(3, 3)

test_graph.BFS(2)


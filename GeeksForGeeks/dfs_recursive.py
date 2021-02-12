from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_nodes = defaultdict(lambda: False)

    def addEdge(self, start_node, end_node):
        self.graph[start_node].append(end_node)

    def isVisited(self, node):
        return self.visited_nodes[node]

    def DFS(self, start_node):
        if self.visited_nodes[start_node]:
            return 

        print(start_node)
        self.visited_nodes[start_node] = True
        for neighbour in self.graph[start_node]:
            self.DFS(neighbour)



# circular graph    
graph = Graph()
graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('C', 'D')
graph.addEdge('B', 'E')
graph.addEdge('D', 'E')

graph.DFS('A')


# graph with 2 node
graph = Graph()
graph.addEdge('A', 'B')

graph.DFS('A')

# graph with triangular node connection
graph = Graph()
graph.addEdge('A', 'B')
graph.addEdge('B', 'C')
graph.addEdge('C', 'A')


graph.DFS('B')
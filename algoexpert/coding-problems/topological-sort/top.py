
graph = {
    'B': ['E', 'C'],
    'E': ['A', 'C'],
    'C': [],
    'A': ['C', 'D'],
    'D': []
}

def topological_sort(graph, start_node):
    # the nodes that has already been visited 
    is_visited = set()
    # the next node to be visited
    to_be_visited = set()
    to_be_visited.add(start_node)

    while len(to_be_visited) != 0: 
        # get the next node to explore 
        node_to_explore = get_node_to_visit(graph, to_be_visited, is_visited)
        if node_to_explore is None:
            break
    
        # insert the child nodes of currently exploring node into to_be_visited
        for child_node in graph[node_to_explore]:
            to_be_visited.add(child_node)

        print(node_to_explore)
        is_visited.add(node_to_explore)

    # all nodes having adjacency list i.e nodes which are prerequisite of another node
    for node in to_be_visited:
        print(node)


def get_node_to_visit(graph, to_be_visited, is_visited):
    for node in to_be_visited:
        # node has not been already visited and has adjacency list
        if node not in is_visited and len(graph[node]) > 0:
            to_be_visited.remove(node)
            return node
    
    return None
    
topological_sort(graph, 'B')
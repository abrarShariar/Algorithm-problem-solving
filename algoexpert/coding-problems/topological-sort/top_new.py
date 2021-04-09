graph = {
    'B': ['E', 'C'],
    'E': ['A', 'C'],
    'C': [],
    'A': ['C', 'D'],
    'D': []
}


def topological_sort(digraph):
    # create an indegress dictionary
    # the in degree represent the node's prerequiste
    in_degree = {node: 0 for node in digraph}
    for node in digraph:
        for neighbour in digraph[node]:
            in_degree[neighbour] = in_degree.get(neighbour, 0) + 1
    
    # the result list
    topological_sort_list = list()
    # the next nodes to visit will be here
    nodes_with_no_incoming_edges = []

    # insert the first node with no incoming edge into the nodes_with_no_incoming_edges
    for node in digraph:
        if in_degree[node] == 0:
            nodes_with_no_incoming_edges.append(node)

    while len(nodes_with_no_incoming_edges) > 0:
        current_node = nodes_with_no_incoming_edges.pop()
        if current_node not in topological_sort_list:
            topological_sort_list.append(current_node)
        
        # update the in degree of the adjacent list node
        for node in digraph[current_node]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                nodes_with_no_incoming_edges.append(node)


    return topological_sort_list

print(topological_sort(graph))

    

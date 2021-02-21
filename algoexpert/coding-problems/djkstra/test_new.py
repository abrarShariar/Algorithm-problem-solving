def dijkstrasAlgorithm(start, edges):
    # initialize a result vertex
    result_list = []

    # set total number of nodes
    total_vertices = len(edges)

    # initialize the distances property
    distances = [float('inf') for i in range(total_vertices)]
    distances[start] = 0

    # update the is_visited list
    is_visited = [False for i in range(total_vertices)]

    # loop over all nodes
    # O(n)
    for i in range(len(edges)):
        # O(n)
        current_node, current_min_distance = getMinNode(distances, is_visited)

        if current_min_distance == float('inf'):
            break

        # loop over the neighbour nodes
        for neighbour in edges[current_node]:
            neighbour_node = neighbour[0]
            edge_distance = neighbour[1]

            current_distance = edge_distance + distances[current_node]
            current_distance = min(current_distance, distances[neighbour_node])
            distances[neighbour_node] = current_distance

        is_visited[current_node] = True
        
    return [-1 if distances[i] == float('inf') else distances[i] for i in range(len(distances))]


def getMinNode(distances, is_visited):
    current_min_node = None
    current_min_distance = float('inf')

    for i in range(len(distances)):
        if not is_visited[i] and distances[i] < current_min_distance:
            current_min_distance = distances[i]
            current_min_node = i
    
    return current_min_node, current_min_distance
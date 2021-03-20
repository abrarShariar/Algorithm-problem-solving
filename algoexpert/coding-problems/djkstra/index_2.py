def dijkstrasAlgorithm(start, edges):
    is_visited = [False] * len(edges)
    min_distance = [float('inf')] * len(edges)
    min_distance[start] = 0
    current_node = start

    while current_node is not None:
        # get the current_node to visit
        current_node = getNextMinNodeToVisit(is_visited, min_distance)
        if current_node is None:
            continue
        # start looping over the neighbours of the current_node
        for neighbour_node in edges[current_node]:
            node = neighbour_node[0]
            path_cost = neighbour_node[1]
            total_cost = path_cost + min_distance[current_node]
            
            if total_cost < min_distance[node]:
                min_distance[node] = total_cost
        
        # after finishing visiting all the neighbour nodes: mark the current_node as visited 
        is_visited[current_node] = True
    
    min_distance = [x if x != float('inf') else -1 for x in min_distance]
    return min_distance


# get the next node to visit with the shortest distance
def getNextMinNodeToVisit(is_visited, min_distance):
    next_node = None
    running_min_distance = float('inf')
    for node in range(len(min_distance)):
        if not is_visited[node] and min_distance[node] < running_min_distance:
            running_min_distance = min_distance[node]
            next_node = node 
    
    return next_node


start = 0
edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    []
]

print(dijkstrasAlgorithm(start, edges))
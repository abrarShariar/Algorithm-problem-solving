def dijkstrasAlgorithm(start, edges):
    visited = set()
    total_number_vertices = len(edges)
    distance = [float('inf') for i in range(total_number_vertices)]

    distance[start] = 0

    while len(visited) < total_number_vertices:
        current_node, min_distance = get_min_node(visited, distance)
        if min_distance == float('inf'):
            break

        visited.add(current_node)
        
        for neighbour in edges[current_node]:
            node = neighbour[0]
            node_distance = neighbour[1]
            if node not in visited:
                if min_distance + node_distance < distance[node]:
                    distance[node] = min_distance + node_distance
        
    return [-1 if x == float('inf') else x for x in distance]

def get_min_node(visited, distance):
    min_node = None
    min_distance = float('inf')

    for i in range(len(distance)):
        if distance[i] < min_distance and i not in visited:
            min_node = i
            min_distance = distance[i] 
    
    return min_node, min_distance

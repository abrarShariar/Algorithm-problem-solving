import math

def dijkstrasAlgorithm(start, edges):
    # create the min_distance dictionary
    min_distance_dict = {}
    for i in range(len(edges)):
        min_distance_dict[i] = math.inf

    # set the start node min distance to 0
    min_distance_dict[start] = 0

    is_visited = set()

    # loop over the edges and update the min_distance dict
    for current_node in range(len(edges)):
        if current_node not in is_visited:
            for i in range(len(edges[current_node])):
                neighbour = edges[current_node][i]
                node = neighbour[0]
                distance = neighbour[1]
                current_distance = min_distance_dict[current_node] + distance
                if current_distance < min_distance_dict[node]:
                    min_distance_dict[node] = current_distance
        
            is_visited.add(current_node)

    return [-1 if value == math.inf else value for key, value in min_distance_dict.items()]


start = 0
edges = [
    [[1,7]],
    [[2,6], [3,20], [4,3]],
    [[3,14]],
    [[4,2]],
    [],
    []
]

print(dijkstrasAlgorithm(start, edges))

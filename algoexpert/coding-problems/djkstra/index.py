import math

def dijkstrasAlgorithm(start, edges): 
    
    # total number of vertices
    total_vertices = len(edges)
    # a min distance list to store the min distance to all nodes
    minDistance = [float('inf') for i in range(total_vertices)]
    # set min distance of start node to 0
    minDistance[start] = 0
    visited = set()

    # loop over each node until all is visited 
    while len(visited) != total_vertices:
        # get the node with minimum distance => visit it
        currentNode, currentMinDistance = getNextMinVertex(visited, minDistance)
        # this part means we only node/nodes that are unvisted 
        if currentMinDistance == float('inf'):
            break
        
        visited.add(currentNode)

        # visit all unvisited neighbours of currentNode
        # update their min distance
        for neighbour in edges[currentNode]:
            node, distance = neighbour 

            if node not in visited:
                current_distance = distance + minDistance[currentNode]
                if current_distance < minDistance[node]:
                    minDistance[node] = current_distance

    return [-1 if val == float('inf') else val for val in minDistance]


# Notice that we are always taking the next node with the smallest distance from the current node
def getNextMinVertex(visited, distance):
    currentMinDistance = float('inf')
    currentMinVertex = None

    for current_node in range(len(distance)):
        if current_node in visited:
            continue

        if distance[current_node] <= currentMinDistance:
            currentMinDistance = distance[current_node]
            currentMinVertex = current_node
    
    return currentMinVertex, currentMinDistance

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

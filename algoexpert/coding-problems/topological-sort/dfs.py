graph = {
    1: [],
    2: [1, 4, 5],
    3: [1, 5],
    4: [],
    5: []
}

is_visited = set()
def dfs(start_node, graph):
    # visit all the negihbours of the start node revursively
    for neighbour in graph[start_node]:
        if neighbour not in is_visited:
            dfs(neighbour, graph)

    print(start_node)
    is_visited.add(start_node)

nodes = [1,2,3,4,5]
for node in nodes:
    if node not in is_visited:
        dfs(node, graph)
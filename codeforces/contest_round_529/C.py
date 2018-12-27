n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n):
    s, e = input().strip().split(' ')
    s, e = [int(s), int(e)]

    graph[s].append(e)
    graph[e].append(s)


def dfsUtil(v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if visited[i] == False:
            dfsUtil(i, visited)

def dfs(graph):
    visited = [False] * (len(graph))
    dfsUtil(1, visited)

dfs(graph)

import math

INFINITY = math.inf

[n, m] = list(map(int, input().split()))
graph = {x: [] for x in range(1, n+1)}

for i in range(m):
	[n1, n2, w] =	list(map(int, input().split()))
	graph[n1].append((n2, w))
	graph[n2].append((n1, w))

def getMinNode(graph, distance, visited):
	min_node = None
	min_distance = INFINITY

	for node in graph.keys():
		if visited[node] == False and distance[node] < min_distance:
			min_distance = distance[node]
			min_node = node

	return min_node

def dks(graph, start_node, end_node):
	visited = {x: False for x in graph.keys()}
	distance = {x: INFINITY for x in graph.keys()}
	parent = {x: None for x in graph.keys()}

	distance[start_node] = 0
	current_node = start_node

	while current_node:
		
		for child_node in graph[current_node]:
			node = child_node[0]
			weight = child_node[1]

			if visited[node] == False:
				current_path_cost = distance[current_node] + weight
				if current_path_cost < distance[node]:
					distance[node] = current_path_cost
					parent[node] = current_node
		
		visited[current_node] = True
		current_node = getMinNode(graph, distance, visited)

	path = [end_node]
	while parent[end_node]:
		path.append(parent[end_node])
		end_node = parent[end_node]

	if len(path) == 1:
		print(-1)
		return

	path.reverse()
	for ch in path:
		print(ch, end=" ")
		
dks(graph, 1, n)
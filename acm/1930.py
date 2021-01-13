
[n, m] = list(map(int,input().split()))
graph = {x: [] for x in range(1, n+1)}

for i in range(m):
	[n1, n2] = list(map(int,input().split()))
	graph[n1].append(n2)
	graph[n2].append(n1)

[start_node, end_node] = list(map(int,input().split()))

def find_shortest_gear(graph, start_node, end_node):
	search_queue = [start_node]
	is_visited = set()
	is_visited.add(start_node)
	gear_counts = -1
	
	while len(search_queue):
		current_node = search_queue.pop(0)
		if current_node == end_node:
			return gear_counts

		gear_counts += 1

		for child_node in graph[current_node]:
			if child_node == end_node:
				return gear_counts

			if child_node not in is_visited:
				search_queue.append(child_node)
				is_visited.add(child_node)

print(find_shortest_gear(graph, start_node, end_node))





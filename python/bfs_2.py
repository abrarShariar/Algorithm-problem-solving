graph = {
	'A': ['B', 'C'],
	'B': ['A', 'D'],
	'C': ['A', 'E', 'F'],
	'D': ['B', 'E', 'G'],
	'E': ['C', 'D'],
	'F': ['C', 'G'],
	'G': ['F', 'D']
}

def bfs(graph, start_node, search_node):
	search_queue = [start_node]
	is_visited = [start_node]

	while len(search_queue) > 0:
		current_node = search_queue.pop(0)
		if current_node == search_node:
			print('Found search node: ', current_node)
			return
		print('Currently visiting: ', current_node)

		for child_node in graph[current_node]:
			if child_node not in is_visited:
				is_visited.append(child_node)
				search_queue.append(child_node)


bfs(graph, 'A', 'G')
		

		



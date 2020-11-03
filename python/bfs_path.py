graph = {
	'A': ['B', 'C'],
	'B': ['A', 'D', 'E'],
	'C': ['A', 'F'],
	'D': ['B'],
	'E': ['B', 'G'],
	'F': ['C', 'H'],
	'G': ['H', 'E'],
	'H': ['F', 'G']
}

def bfs(graph, start_node, end_node):
	path = generated_path(graph, start_node)
	# print(path)
	distance = calculate_distance(start_node, end_node, path)
	return distance

def	calculate_distance(start_node, end_node, path):
	current_node = end_node
	distance = 0
	while path[current_node]:
		distance += 1
		current_node = path[current_node]

	if current_node == start_node:
		return distance
	return -1

def generated_path(graph, start_node):
	search_queue = [start_node]
	is_visited = set()
	is_visited.add(start_node)

	path = {}
	# initialize path
	for node in graph.keys():
		path[node] = None
		
	while len(search_queue):
		current_node = search_queue.pop(0)
		
		for child_node in graph[current_node]:
			if child_node not in is_visited:
				is_visited.add(child_node)
				search_queue.append(child_node)
				path[child_node] = current_node

	return path

print(bfs(graph, 'A', 'D'))
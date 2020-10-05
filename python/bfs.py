graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def bfs(graph, startNode):
	visited = [startNode]
	queue = [startNode]
	
	while len(queue) > 0:
		# get the top item from the queue
		current_node = queue.pop(0)
		print(current_node)

		for child_node in graph[current_node]:
			if current_node not in visited:
				visited.append(current_node)
				queue.append(child_node)


bfs(graph, 'A')
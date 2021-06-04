def find_center_node(edges):
	graph = {}
	node_count = len(edges) + 1

	# O(n)
	for i in range(1, node_count + 1):
		graph[i] = set()

	# O(E)
	for edge in edges:
		node_u = edge[0]
		node_v = edge[1]

		graph[node_u].add(node_v)
		graph[node_v].add(node_u)

	# O(n)
	for key, value in graph.items():
		if len(value) == node_count - 1:
			return key


print(find_center_node([[1,2],[2,3],[4,2]]))
print(find_center_node([[1,2],[5,1],[1,3],[1,4]]))


import math
INFINITY = math.inf

graph = { 
	'B': [('P', 0), ('LP', 5)],
	'P': [('G', 30), ('DS', 35)],
	'LP': [('G', 15), ('DS', 20)],
	'G': [('Pi', 20)],
	'DS': [('Pi', 10)],
	'Pi': []
};

def dks(graph, start_node, end_node):
	cost_dict = {}
	parent_dict = {}

	cost_dict[start_node] = 0
	parent_dict[start_node] = None

	search_queue = [start_node]

	while len(search_queue):
		current_node = search_queue.pop(0)

		# visit its child nodes
		for child_node in graph[current_node]:
			node = child_node[0]
			weight = child_node[1]

			current_path_cost = cost_dict[current_node] + weight

			if current_path_cost < cost_dict.get(node, INFINITY):
				cost_dict[node] = current_path_cost
				parent_dict[node] = current_node
			
			if node not in search_queue:
				search_queue.append(node)

	# print(cost_dict)
	# print(parent_dict)

	# shortest path costs
	print("Shortest path from B -> Pi costs: ", cost_dict[end_node])
	# print the path
	path = [end_node]
	while not (parent_dict[end_node] == None):
		path.append(parent_dict[end_node])
		end_node = parent_dict[end_node]
	
	print(path)


dks(graph, 'B', 'Pi')
		







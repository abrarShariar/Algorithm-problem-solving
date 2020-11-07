import math
INFINITY = math.inf

# a weighted graph
graph = {
	'a': [('c', 20), ('b', 10)],
	'b': [('e', 10), ('d', 50)],
	'c': [('d', 20), ('e', 33)],
	'd': [('e', 20), ('f', 2)],
	'e': [('f', 1)],
	'f': []
}

def getMinNode(graph, distance, visited):
	min_node = ''
	min_distance = INFINITY

	for node in graph.keys():
		if visited[node] == False and distance[node] < min_distance:
			min_distance = distance[node]
			min_node = node

	return min_node

def dks(graph, start_node):
	visited = {x: False for x in graph.keys()}
	distance = {x: INFINITY for x in graph.keys()}

	distance[start_node] = 0
	current_node = start_node

	while current_node:
		for child_node in graph[current_node]:
			node = child_node[0]
			weight = child_node[1]
			current_path_cost = distance[current_node] + weight

			if current_path_cost < distance[node]:
				distance[node] = current_path_cost
			
		visited[current_node] = True
		# select the node with
		current_node = getMinNode(graph, distance, visited)

	return distance

print(dks(graph, 'a'))

# import math
# INFINITY = math.inf

# graph = { 
# 	'B': [('P', 0), ('LP', 5)],
# 	'P': [('G', 30), ('DS', 35)],
# 	'LP': [('G', 15), ('DS', 20)],
# 	'G': [('Pi', 20)],
# 	'DS': [('Pi', 10)],
# 	'Pi': []
# };

# def dks(graph, start_node, end_node):
# 	cost_dict = {}
# 	parent_dict = {}

# 	cost_dict[start_node] = 0
# 	parent_dict[start_node] = None

# 	search_queue = [start_node]

# 	while len(search_queue):
# 		current_node = search_queue.pop(0)

# 		# visit its child nodes
# 		for child_node in graph[current_node]:
# 			node = child_node[0]
# 			weight = child_node[1]

# 			current_path_cost = cost_dict[current_node] + weight

# 			if current_path_cost < cost_dict.get(node, INFINITY):
# 				cost_dict[node] = current_path_cost
# 				parent_dict[node] = current_node
			
# 			if node not in search_queue:
# 				search_queue.append(node)

# 	# print(cost_dict)
# 	# print(parent_dict)

# 	# shortest path costs
# 	print("Shortest path from B -> Pi costs: ", cost_dict[end_node])
# 	# print the path
# 	path = [end_node]
# 	while not (parent_dict[end_node] == None):
# 		path.append(parent_dict[end_node])
# 		end_node = parent_dict[end_node]
	
# 	print("The shortest path: ")
# 	path.reverse()
# 	print(" -> ".join(path))


# dks(graph, 'B', 'Pi')
		







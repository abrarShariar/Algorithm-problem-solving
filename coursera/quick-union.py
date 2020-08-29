
class QuickUnion:
	
	def __init__(self, total_nodes):
		self.node_list = [None] * total_nodes
		for i in range(total_nodes):
			self.node_list[i] = i

	# the union is quick compared to the find
	def union(self, first_node, second_node):
		first_node_root = self.find_root(first_node)
		second_node_root = self.find_root(second_node)
		# connect
		self.node_list[first_node_root] = second_node_root
		
	# the find takes more time here
	def find_root(self, node):
		if self.node_list[node] == node:
			return self.node_list[node]

		return self.find_root(self.node_list[node])

	# check if connected
	def is_connected(self, first_node, second_node):
		return self.find_root(first_node) == self.find_root(second_node)
		
test_union = QuickUnion(10)
print(test_union.node_list)

test_union.union(4,3)
print(test_union.node_list)

test_union.union(3,8)
print(test_union.node_list)

test_union.union(9,4)
print(test_union.node_list)

test_union.union(6,5)
print(test_union.node_list)

print(test_union.is_connected(8,9))
print(test_union.is_connected(5,4))
print(test_union.is_connected(8,4))
print(test_union.is_connected(9,4))
print(test_union.is_connected(5,6))
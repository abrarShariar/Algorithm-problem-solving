class UnionFind:
	def __init__(self, max_node):
		self.node_list = [None] * (max_node + 1)
		# populate the nodes with the initial data
		for i in range(max_node + 1):
			self.node_list[i] = i

	def union(self,first_node, second_node):
		# connect 'em
		# first_node = to be changed
		# second_node = one who changes
		first_node_val = self.node_list[first_node]
		second_node_val = self.node_list[second_node]
		# scan the whole list to find the node
		for i in range(len(self.node_list)):
			if self.node_list[i] == first_node_val:
				self.node_list[i] = second_node_val


testU = UnionFind(9)
testU.union(4, 3)
testU.union(3, 8)
testU.union(6, 5)
testU.union(9, 4)
testU.union(2, 1)
testU.union(5, 0)
testU.union(7, 2)
testU.union(6, 1)


print(testU.node_list)




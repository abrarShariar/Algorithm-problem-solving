# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
# TO BE CONTINUED
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		elif value >= self.value:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
					
	def contains(self, value):
		if self.value == value:
			return True
		
		if value > self.value:
			if self.right is not None:
				return self.right.contains(value)
			else:
				return False
		else:
			if self.left is not None:
				return self.left.contains(value)
			else:
				return False

	# doing it the iterative way
	def remove(self, value, current_root = None):
		# find the node to remove first
		# then apply these three conditions for removing:
			# 1. if leaf node = make the parent point to None
			# 2. if only one sub tree (left/right) = make the parent point to that sub-tree
			# 3. if both sub-tree is present (left+right) = find the minimum from right sub-tree and replace with the node to be removed 

		node_to_remove = self
		# track the parent node of the node_to_removoe
		while node_to_remove is not None:
			if node_to_remove.value == value:
				break
			
			elif value < node_to_remove.value:
				current_root = node_to_remove
				node_to_remove = node_to_remove.left
			else:
				current_root = node_to_remove
				node_to_remove = node_to_remove.right

		if node_to_remove is None:
			return
			
		# 1. leaf node
		if node_to_remove.left == None and node_to_remove.right == None:
			if current_root.left == node_to_remove:
				current_root.left = None
			else:
				current_root.right = None

		# 2. if only right OR left sub-tree we have for the node_to_remove
		elif node_to_remove.left == None and node_to_remove.right != None:
			if node_to_remove == current_root.left:
				current_root.left = node_to_remove.right
			else:
				current_root.right = node_to_remove.right
		elif node_to_remove.right == None and node_to_remove.left != None:
			if node_to_remove == current_root.left:
				current_root.left = node_to_remove.left
			else:
				current_root.right = node_to_remove.left
		
		# if both left and right sub-tree is present
		elif node_to_remove.left != None and node_to_remove.right != None:
			# find the min node in the right sub tree
			node_to_replace = self.find_min_node(node_to_remove)
			node_to_remove.value, node_to_replace.value = node_to_replace.value, node_to_remove.value

			# remove the node_to_replace
			node_to_remove.remove(node_to_replace.value, node_to_remove)


	def find_min_node(self, current_root):
		# the leftmost node is the minimum node
		while current_root.left:
			current_root = current_root.left
		
		return current_root

	def test_print_inorder(self):
		# print the left sub tree
		if self.left is not None:
			self.left.test_print_inorder()
		# print root
		print(self.value)
		# print the right sub-tree
		if self.right is not None:
			self.right.test_print_inorder()

# bst = BST(10)
# bst.insert(15)
# bst.insert(2)
# bst.insert(100)
# bst.insert(1000)

# # bst.test_print_inorder()
# print(bst.contains(2))
# print(bst.contains(10000))

# # bst.test_print_inorder()
# bst.remove(2)
# bst.test_print_inorder()


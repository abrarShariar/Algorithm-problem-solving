class Node:
	def __init__(self, left = None, right = None, value = None):
		self.left = left
		self.right = right
		self.value = value

class BinaryTree:
	def __init__(self, root = None):
		self.root = root
	
	def insertNode(self, current_root = None, new_value = 0):
		if current_root is None:
			return
		
		elif new_value < current_root.value:
			if current_root.left is None:
				current_root.left = Node(value = new_value)
			else:
				self.insertNode(current_root.left, new_value)

		elif new_value >= current_root.value:
			if current_root.right is None:
				current_root.right = Node(value = new_value)
			else:
				self.insertNode(current_root.right, new_value)

	# print tree In-Order traversal - CORRECT
	def inOrderTraversal(self, current_root = None):
		if current_root is None:
			return
			
		# if there's a left sub-tree - explore it first
		self.inOrderTraversal(current_root.left)
		print(current_root.value)
		self.inOrderTraversal(current_root.right)

	# print tree in post-order traversal 
	def postOrderTraversal(self, current_root = None):
		if current_root is None:
			return
		
		# traverse left sub-tree
		self.postOrderTraversal(current_root.left)
		# traverse right sub-tree
		self.postOrderTraversal(current_root.right)
		# print the root
		print(current_root.value)
	
	# print tree in pre-order traversal
	def preOrderTraversal(self, current_root):
		if current_root is None:
			return
		
		print(current_root.value)
		self.preOrderTraversal(current_root.left)
		self.preOrderTraversal(current_root.right)


bin_tree = BinaryTree(Node(value = 27))
bin_tree.insertNode(bin_tree.root, new_value = 14)
bin_tree.insertNode(bin_tree.root, new_value = 35)
bin_tree.insertNode(bin_tree.root, new_value = 10)
bin_tree.insertNode(bin_tree.root, new_value = 19)
bin_tree.insertNode(bin_tree.root, new_value = 31)
bin_tree.insertNode(bin_tree.root, new_value = 42)

# bin_tree.inOrderTraversal(bin_tree.root)
bin_tree.preOrderTraversal(bin_tree.root)







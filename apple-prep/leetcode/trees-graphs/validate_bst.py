# This is an input class. Do not edit.
# PASSED
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def validateBst(tree, max = float('inf'), min = float('-inf')):
	if tree is None:
		return True
	
	if tree.value >= max or tree.value < min:
		return False

	# if left sub tree - set the max value
	# if right sub-tree - set the min value
	return validateBst(tree.left, max = tree.value, min = min) and validateBst(tree.right, max = max, min = tree.value)



















# # This is an input class. Do not edit.
# # In Progress
# class BST:
# 	def __init__(self, value):
# 		self.value = value
# 		self.left = None
# 		self.right = None

# def validateBst(tree):
# 	current_node = tree

# 	# do a tree traversal
# 	return travserse_o_shit(current_node)

# def travserse_o_shit(current_node):
# 	if current_node.left:
# 		if current_node.left.value > current_node.value:
# 			return False

# 		if current_node.left.right and current_node.left.right.value < current_node.left.value:
# 			return False

# 		if current_node.left.left and current_node.left.left.value > current_node.left.value:
# 			return False

# 		else:
# 			return travserse_o_shit(current_node.left)
	
# 	if current_node.right:
# 		if current_node.right.value < current_node.value:
# 			return False

# 		if current_node.right.right and current_node.right.right.value < current_node.right.value:
# 			return False

# 		if current_node.right.left and current_node.right.left.value > current_node.right.value:
# 			return False

# 		else:
# 			return travserse_o_shit(current_node.right)

# 	else:
# 		return True

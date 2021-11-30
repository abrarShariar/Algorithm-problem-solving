# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
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


	def remove(self, value):
		# Write your code here.
		# Do not edit the return statement of this method.
		return self

	def test_print_inorder(self):
		# print the left sub tree
		if self.left is not None:
			self.left.test_print_inorder()
		# print root
		print(self.value)
		# print the right sub-tree
		if self.right is not None:
			self.right.test_print_inorder()

bst = BST(10)
bst.insert(15)
bst.insert(2)
bst.insert(100)
bst.insert(1000)



# bst.test_print_inorder()
print(bst.contains(2))
print(bst.contains(10000))


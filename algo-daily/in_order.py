def inorder(root):
	if root == None:
		return
	in_order(root.left)
	print(root.val)
	in_order(root.right)
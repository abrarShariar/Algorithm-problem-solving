def preOrder(root):
    if root is None:
        return root
    
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
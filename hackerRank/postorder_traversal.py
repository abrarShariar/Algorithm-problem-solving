def postOrder(root):
    if root is None:
        return root
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=" ")

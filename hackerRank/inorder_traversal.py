def inOrder(root):
    #Write your code here
    if root is None:
        return root
    
    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)

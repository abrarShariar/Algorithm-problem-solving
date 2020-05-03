

# method for bfs travel
def bfs_travel(root):
    que = []
    while root != None:
        print(root.value)
        if root.left != None:
            que.append(root.left)
        if root.right != None:
            que.append(root.right)
        
        if len(que) <= 0:
            return 
        root = que.pop(0)


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# make tress for testing
tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)

# bfs_travel(tree)

# make tress for testing
tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right = right.insert_right(4)
right.insert_left(18)
right.insert_right(11)

bfs_travel(tree)







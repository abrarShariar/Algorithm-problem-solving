class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node = Node(10)
node.left = Node(5)
node.right = Node(20)
node.left.left = Node(1)
node.left.right = Node(2)
node.right.left = Node(11)
node.right.right = Node(50)


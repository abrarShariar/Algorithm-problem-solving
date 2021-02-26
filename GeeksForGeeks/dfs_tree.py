class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)

def in_order_traversal(root):
    # left -> root -> right
    if root:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value)

# in_order_traversal(node)
# pre_order_traversal(node)
post_order_traversal(node)
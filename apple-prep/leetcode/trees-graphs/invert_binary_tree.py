# recursive solution - SOLVED
def invertBinaryTree(tree):
    if tree is None:
        return

    current_root = tree
    left_child, right_child = current_root.left, current_root.right
    current_root.left = right_child
    current_root.right = left_child

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

# iterativee solution
def invertBinaryTree(tree):
    node_queue = [tree]
    while len(node_queue) > 0:
        current_node = node_queue.pop(0)

        # this is a child node
        if current_node is None:
            continue

        left_child_node = current_node.left
        right_child_node = current_node.right
        current_node.right, current_node.left = left_child_node, right_child_node

        node_queue.append(current_node.left)
        node_queue.append(current_node.right)

    return tree




# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
    current_depth = 0
    return running_node_sum(root, current_depth)

def running_node_sum(node, current_dept):
    # a node which is None is of value zero
    if node is None:
        return 0

    # increase the current_dept and pass as a runnning sum
    return current_dept + running_node_sum(node.left, current_dept + 1) + running_node_sum(node.right, current_dept + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

binT = BinaryTree(1)
binT.left = BinaryTree(2)
binT.right = BinaryTree(3)

print(nodeDepths(binT))
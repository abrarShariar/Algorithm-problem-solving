# see: https://www.youtube.com/watch?v=MILxfAbIhrE

def is_binary_search_tree(root):
    if root == None:
        return False

    nodes_and_bounds = [(root, -float('INF'), float('INF')]

    while len(nodes_and_bounds):
        node, lower, upper = nodes_and_bounds.pop()

        if node.value < lower or node.value > upper:
            return False

        if node.left != None:
            nodes_and_bounds.append((node.left, lower, node.value))

        if node.right != None:
            nodes_and_bounds.append((node.right, node.value, upper))

        return True



# def dfs_recur(root, lower, upper):
#     if root == None:
#         return
    
#     print(root.value)
#     if root.left != None:
#         if root.left.value > upper:
#             return False
#         upper = root.left.value
#         dfs_recur(root.left, lower, upper)
    
#     if root.right != None:
#         if not (root.right.value > lower and root.right.value < upper):
#             return False
#         upper = root.right.value
#         dfs_recur(root.right, lower, upper)

#     return True



class BinaryTreeNode():

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


tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(80)
left.insert_left(20)
left.insert_right(60)
right.insert_right(99)

print(dfs_recur(tree, 0, tree.value))

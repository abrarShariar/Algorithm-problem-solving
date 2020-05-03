import unittest

# DFS Solve
def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    if tree_root is None:
        return True

    nodes = []
    depths = []
    nodes.append((tree_root, 0))

    while len(nodes):
        # nodes is used like a stack here (node, depth) -> tupple
        node, depth = nodes.pop()
        # reached a leaf
        if node.left == None and node.right == None:
            if depth not in depths:
                depths.append(depth)
            
            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                return False
        # not a leaf
        else:
            if node.left:
                nodes.append((node.left, depth+1))
            if node.right:
                nodes.append((node.right, depth+1))

    return True

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
# tree = BinaryTreeNode(5)
# left = tree.insert_left(8)
# right = tree.insert_right(6)
# left.insert_left(1)
# left.insert_right(2)
# right.insert_left(3)
# right.insert_right(4)

# # bfs_travel(tree)

# # make tress for testing
# tree = BinaryTreeNode(5)
# left = tree.insert_left(8)
# right = tree.insert_right(6)
# left.insert_left(1)
# left.insert_right(2)
# right.insert_left(3)
# right = right.insert_right(4)
# right.insert_left(18)
# right.insert_right(11)

# bfs_travel(tree)

# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_both_subtrees_superbalanced_two(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        right = tree.insert_right(4)
        left.insert_left(3)
        left_right = left.insert_right(7)
        left_right.insert_right(8)
        right_right = right.insert_right(5)
        right_right_right = right_right.insert_right(6)
        right_right_right.insert_right(9)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_at_different_levels(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        left_left = left.insert_left(3)
        left.insert_right(4)
        left_left.insert_left(5)
        left_left.insert_right(6)
        right = tree.insert_right(7)
        right_right = right.insert_right(8)
        right_right_right = right_right.insert_right(9)
        right_right_right.insert_right(10)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
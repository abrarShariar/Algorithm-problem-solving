import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        que=[]
        depth=0
        que.append(root)
        d_x, d_y, p_x, p_y = 0, 0, 0, 0
        node_count = 0
        depth = 0
        while len(que):
            node = que.pop(0)
            node_count += 1
            depth = math.ceil(math.log2(node_count+1))
            print(depth)
            if node.left:
                que.append(node.left)
                if (node.left.val == x):
                    d_x = depth
                    p_x = node.val
                if (node.left.val == y):
                    d_y = depth
                    p_y = node.val
            if node.right:
                que.append(node.right)
                if (node.right.val == x):
                    d_x = depth
                    p_x = node.val
                if (node.right.val == y):
                    d_y = depth
                    p_y = node.val
        
        if (d_x == d_y) and (p_x != p_y):
                return True
        return False

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(5)
node.left.right = TreeNode(4)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

x = Solution()
print(x.isCousins(node, 5, 6))
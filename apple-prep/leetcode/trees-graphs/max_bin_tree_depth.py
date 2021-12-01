# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		return self.findMaxDepth(root, 0)
		
	def findMaxDepth(self, current_root, max_sum = 0):
		if current_root is None:
			return max_sum
		
		return max(self.findMaxDepth(current_root.left, max_sum + 1),
					self.findMaxDepth(current_root.right, max_sum + 1))


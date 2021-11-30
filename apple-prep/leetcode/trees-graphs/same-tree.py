# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		# do a traversal parallely to both trees and match each

		# if both are None - we are same
		if p == None and q == None:
			return True
		# if either one of them is None but not both - FALSE
		elif p == None or q == None: 
			return False

		# if vvalue doesn't match - FALSe
		if p.val != q.val:
			return False
		
		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 



 
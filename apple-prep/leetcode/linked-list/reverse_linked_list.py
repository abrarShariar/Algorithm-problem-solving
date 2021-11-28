# Definition for singly-linked list.
# SOLVED
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		res_head = None
		current_head = head

		while current_head:
			new_node = ListNode(current_head.val)
			new_node.next = res_head
			res_head = new_node
			current_head = current_head.next
		
		return res_head

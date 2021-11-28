# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		head_l1 = list1
		head_l2 = list2

		res_head = ListNode()
		current_head = res_head

		while head_l1 and head_l2:
			next_node = ListNode()
			if head_l1.val < head_l2.val:
				current_head.next = head_l1
				head_l1 = head_l1.next
			elif head_l2.val <= head_l1.val:
				current_head.next = head_l2
				head_l2 = head_l2.next
			
			current_head = current_head.next

		if head_l1:
			current_head.next = head_l1
		
		if head_l2:
			current_head.next = head_l2
		
		return res_head.next
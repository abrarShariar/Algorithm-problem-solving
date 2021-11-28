# SOLVED
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		head_l1 = l1
		head_l2 = l2
		result_head = None
		current_head = None
		count_over_digit = 0
		rem_digit = 0

		while head_l1 or head_l2:
			current_l1_val = 0
			current_l2_val = 0
			if head_l1:
				current_l1_val = head_l1.val
			if head_l2:
				current_l2_val = head_l2.val

			current_sum = current_l1_val + current_l2_val + count_over_digit
			count_over_digit = current_sum // 10
			rem_digit = current_sum % 10
			
			if current_sum > 9:
				current_sum = rem_digit
			else:
				count_over_digit = 0

			new_node = ListNode(current_sum) 
			if result_head is None:
				result_head = new_node
				current_head = result_head
			else:
				current_head.next = new_node
				current_head = current_head.next

			if head_l1:
				head_l1 = head_l1.next
			if head_l2:
				head_l2 = head_l2.next
		
		if count_over_digit > 0:
			new_node = ListNode(count_over_digit)
			current_head.next = new_node
				
		return result_head
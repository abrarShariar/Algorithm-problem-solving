# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        start_odd = head
        start_even = head.next
        e_begin = start_even
        # if start_odd == None or start_even == None:
        #     return head
        
        while start_odd != None and start_even != None:
            start_odd.next = start_even.next
            if start_odd.next == None:
                break
            start_odd = start_odd.next
            start_even.next = start_odd.next
            if start_even.next == None:
                break
            start_even = start_even.next

        start_odd.next = e_begin
        return head
            


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
# node.next.next.next.next = ListNode(5)

x = Solution()
ll = x.oddEvenList(node)
print(ll.val)
print(ll.next.val)
print(ll.next.next.val)
print(ll.next.next.next.val)
print(ll.next.next.next.next.val)
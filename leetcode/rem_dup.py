# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        current = head
        nx = head.next 
        while nx != None:
            if current.val == nx.val:
                # freeze the current and move the next
                while nx != None and nx.val == current.val:
                    nx = nx.next
                current.next = nx 
            if nx == None:
                break
            current = nx
            nx = nx.next
        
        return head

node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)
x = Solution()

n = x.deleteDuplicates(node)
print(n.val)
print(n.next.val)
print(n.next.next.val)
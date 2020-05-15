# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None:
            return
        input_list = []
        while head:
            input_list.append(head.val)
            head = head.next
        
        stack = []
        n = len(input_list)
        output_list = [0 for i in range(n)]

        for i in range(n):
            while len(stack) and input_list[stack[-1]] < input_list[i]:
                j = stack.pop()
                output_list[j] = input_list[i]
            stack.append(i)

        return output_list
        
        
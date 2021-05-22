# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slow_p = head.next
    fast_p = head.next.next

    while slow_p != fast_p:
        slow_p = slow_p.next
        fast_p = fast_p.next.next

    slow_p = head
    while slow_p != fast_p:
        slow_p = slow_p.next
        fast_p = fast_p.next

    return slow_p
    

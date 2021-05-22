# This is an input class. Do not edit.
# SOLVED
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    # find the length of the linked list
    ll_len = 0
    start_node = head
    while start_node:
        ll_len += 1
        start_node = start_node.next

    node_to_del_pos = ll_len - k
    
    # this is the head
    if node_to_del_pos <= 0:
        head.value = head.next.value
        head.next = head.next.next
    else:    
        start_node = head
        counter = 0
        while start_node and counter < node_to_del_pos - 1:
            start_node = start_node.next
            counter += 1

        if start_node.next:
            start_node.next = start_node.next.next
        else:
            start_node.next = None



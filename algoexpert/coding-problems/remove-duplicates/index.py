# This is an input class. Do not edit.
# SOLVED
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    first_head = linkedList
    second_head = first_head.next
    if second_head is None:
        return first_head


    # loop till the end of the list
    # O(n)
    while second_head is not None:
        while second_head is not None and first_head.value == second_head.value:
            # keep moving the second head while keeping the first head static
            second_head = second_head.next

        first_head.next = second_head

        if first_head.next is None:
            break

        first_head = second_head
        second_head = second_head.next

    return linkedList


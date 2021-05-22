# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    p1 = linkedListOne
    p2 = linkedListTwo
    carry = 0
    result_head = None
    new_ll = result_head

    while p1 and p2:
        current_sum = int(p1.value) + int(p2.value) + carry
        temp_str = str(current_sum)
        if current_sum > 10:
            carry = int(temp_str[:-1])
        
        new_node = LinkedList(int(temp_str[-1]))
        if new_ll:
            new_ll.next = new_node
            new_ll = new_ll.next
        else:
            result_head = new_node
            new_ll = result_head

        p1 = p1.next
        p2 = p2.next

    # if first linkedlist is still remaining to the end
    while p1:
        current_sum = int(p1.value) + carry
        temp_str = str(current_sum)
        if current_sum > 10:
            carry = int(temp_str[:-1])

        new_node = LinkedList(int(temp_str[-1]))
        new_ll.next = new_node
        new_ll = new_ll.next
        p1 = p1.next

    while p2:
        current_sum = int(p1.value) + carry
        temp_str = str(current_sum)
        if current_sum > 10:
            carry = int(temp_str[:-1])

        new_node = LinkedList(int(temp_str[-1]))
        new_ll.next = new_node
        new_ll = new_ll.next
        p2 = p2.next

    return result_head



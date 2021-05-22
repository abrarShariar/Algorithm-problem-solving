# This is an input class. Do not edit.
# SOLVED
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    p1 = linkedListOne
    p2 = linkedListTwo
    carry = 0
    result_ll = LinkedList(0)
    start_p = result_ll

    # keep going if there is p1 and p2
    while p1 or p2:
        d1, d2 = 0, 0
        if p1:
            d1 = p1.value
        if p2:
            d2 = p2.value

        current_sum = d1 + d2 + carry
        carry = current_sum // 10
        current_num = current_sum % 10

        new_node = LinkedList(current_num)
        start_p.next = new_node
        start_p = start_p.next

        if p1:
            p1 = p1.next
        
        if p2:
            p2 = p2.next

    while carry > 0:
        current_num = carry % 10
        carry = carry // 10
        new_node = LinkedList(current_num)
        start_p.next = new_node
        start_p = start_p.next

    return result_ll.next
    



    

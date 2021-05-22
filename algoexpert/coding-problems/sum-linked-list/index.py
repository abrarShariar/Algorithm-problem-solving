# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# def sumOfLinkedLists(linkedListOne, linkedListTwo):
#     str_1 = ''
#     str_2 = ''

#     ll_p1 = linkedListOne
#     while ll_p1:
#         str_1 += str(ll_p1.value)
#         ll_p1 = ll_p1.next

#     sum1 = int(str_1[::-1])

#     ll_p2 = linkedListTwo
#     while ll_p2:
#         str_2 += str(ll_p2.value)
#         ll_p2 = ll_p2.next
    
#     sum2 = int(str_2[::-1])

#     total_sum = str(sum1 + sum2)

#     head = LinkedList(total_sum[0])
#     start_node = head

#     for i in range(1, len(total_sum)):    
#         start_node.next = LinkedList(total_sum[i])
#         start_node = start_node.next
    
#     return head


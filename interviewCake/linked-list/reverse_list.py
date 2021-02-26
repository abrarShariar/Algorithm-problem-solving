import unittest

# SOLUTION: with 2 pointers 
def kth_to_last_node(k, head):
    if k <= 0:
        raise Exception

    p1 = head
    p2 = head

    counter = 1
    while counter < k and p2:
        counter += 1
        p2 = p2.next

    if p2 is None:
        raise Exception

    while p2.next:
        p1 = p1.next
        p2 = p2.next

    return p1

    

# SOLUTION: with length of the linked list
# def kth_to_last_node(k, head):

#     # Return the kth to last node in the linked list
#     length_of_list = 0
    
#     start_node = head
#     while start_node:
#         length_of_list += 1
#         start_node = start_node.next
    
#     if k > length_of_list or k <= 0:
#         raise Exception 
        
#     start_node = head
#     for i in range(0, length_of_list - k):
#         start_node = start_node.next
    
#     return start_node 


# Tests
class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)
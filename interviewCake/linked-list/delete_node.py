import unittest

def delete_node(node_to_delete):
    # Delete the input node from the linked list
    if node_to_delete.next:
        node_to_delete.value = node_to_delete.next.value
        node_to_delete.next = node_to_delete.next.next
    else:
        raise Exception("This node cannot be deleted?!")
        
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

    def test_node_at_beginning(self):
        delete_node(self.first)
        actual = self.first.get_values()
        expected = [2, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_in_middle(self):
        delete_node(self.second)
        actual = self.first.get_values()
        expected = [1, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_at_end(self):
        with self.assertRaises(Exception):
            delete_node(self.fourth)

    def test_one_node_in_list(self):
        unique = Test.LinkedListNode(1)
        with self.assertRaises(Exception):
            delete_node(unique)


unittest.main(verbosity=2)
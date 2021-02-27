import unittest
# SOLVED
class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # insert item into stack1
        self.stack1.append(item)

    def dequeue(self):
        # check if stack2 is empty
        # if yes => move all elements from stack1 to stack2 until stack1 is empty
        # pop the top element 
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                item = self.stack1.pop()
                self.stack2.append(item)
        
        if not self.stack2:
            raise Exception
        
        return self.stack2.pop()

# Tests

class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)
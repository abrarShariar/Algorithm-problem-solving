import unittest
# SOLVED
class Stack:

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)


    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):

    # Implement the push, pop, and get_max methods
    def __init__(self):
        super().__init__()
        self.max_stack = []
        self.current_max = 0

    def push(self, item):
        if item >= self.current_max:
            self.max_stack.append(item)
            self.current_max = item
        
        super().push(item)

    def pop(self):
        item = super().pop()
        if len(self.max_stack) > 0:
            if item == self.max_stack[-1]:
                self.max_stack.pop()
                if len(self.max_stack) == 0:
                    self.current_max = 0
        
        return item

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

# max_stack = MaxStack()
# max_stack.push(50)
# max_stack.push(3)
# max_stack.push(1)
# max_stack.push(2)
# max_stack.push(4)
# max_stack.push(5)

# print(max_stack.get_max())


# Tests
class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)
        
        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
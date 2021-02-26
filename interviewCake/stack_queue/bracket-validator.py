import unittest
# SOLVED
def is_valid(code):

    # Determine if the input code is valid
    bracket_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    opening_brackets = ['(', '{', '[']
    bracket_stack = []
    for ch in code:
        if ch in opening_brackets:
            bracket_stack.append(ch)
        else:
            if len(bracket_stack) <= 0:
                return False
            top_item = bracket_stack.pop()
            if bracket_dict[ch] != top_item:
                return False
    
    return len(bracket_stack) == 0

# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
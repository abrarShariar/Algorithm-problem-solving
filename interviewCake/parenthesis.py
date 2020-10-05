# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
# Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).


import unittest

def get_closing_paren(sentence, opening_paren_index):
	
	parenthesis_count = 0

	for i in range(opening_paren_index, len(sentence)):
		ch = sentence[i]
		if ch == '(':
			parenthesis_count += 1
		elif ch == ')':
			parenthesis_count -= 1
		
		if parenthesis_count == 0:
			return i

	if parenthesis_count > 0:
		raise Exception()

# def get_closing_paren(sentence, opening_paren_index):
	
# 	paren_stack = []

# 	for i in range(len(sentence)):
# 		if i >= opening_paren_index:
# 			if sentence[i] == '(':
# 				paren_stack.append('(')
# 			elif sentence[i] == ')':
# 				paren_stack.pop()

# 			if len(paren_stack) == 0:
# 				return i

# 	if len(paren_stack) > 0:
# 		raise Exception()

# Tests
class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)

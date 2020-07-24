import unittest

def fizz_buzz(n):
	result = ''
	for i in range(1, n+1):
		temp = ''
		# if i%3 == 0 and i%5 == 0:
		# 	result += 'fizzbuzz'
		if i%3 == 0:
			temp += 'fizz'
		if i%5 == 0:
			temp += 'buzz'
		if temp == '':
			temp += str(i)

		result += temp
		
	return result


class Test(unittest.TestCase):
	def test_two_lists_with_no_intersection (self):
		actual = fizz_buzz(15)
		expected = '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'
		self.assertEqual(actual, expected)

	# def test_two_lists_with_1_intersection (self):

	# 	self.assertEqual(actual, expected)
	
	# def test_two_lists_with_1_item_no_intersection (self):

	# 	self.assertEqual(actual, expected)

	# def test_two_lists_with_1_intersection_2 (self):

	# 	self.assertEqual(actual, expected)

unittest.main(verbosity=2)   
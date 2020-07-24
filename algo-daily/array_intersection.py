import unittest


def intersection (list1, list2):
	# convert lists to dict
	dict1 = {}
	dict2 = {}
	result = []

	for item in list1:
		dict1[item] = dict1.get(item, 0) + 1
		
	for item in list2:
		dict2[item] = dict2.get(item, 0) + 1
	
	for key in dict1.keys():
		if dict2.get(key, 0) > 0:
			result.append(key)
	
	return result


class Test(unittest.TestCase):
	def test_two_lists_with_no_intersection (self):
		l1 = [6,0,12,10,16]
		l2 = [3,15,18,20,15]
		actual = intersection(l1, l2)
		expected = []
		self.assertEqual(actual, expected)

	def test_two_lists_with_1_intersection (self):
		l1 = [1,5,2,12,6]
		l2 = [13,10,9,5,8]
		actual = intersection(l1, l2)
		expected = [5]
		self.assertEqual(actual, expected)
	
	def test_two_lists_with_1_item_no_intersection (self):
		l1 = [3]
		l2 = [15]
		actual = intersection(l1, l2)
		expected = []
		self.assertEqual(actual, expected)

	def test_two_lists_with_1_intersection_2 (self):
		l1 = [2,16,8,9]
		l2 = [14,15,2,20]
		actual = intersection(l1, l2)
		expected = [2]
		self.assertEqual(actual, expected)

unittest.main(verbosity=2)      

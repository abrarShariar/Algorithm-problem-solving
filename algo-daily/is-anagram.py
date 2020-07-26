import unittest

def is_anagram(str1, str2):
	# convert to dicts
	dict1 = {}
	dict2 = {}

	for st in str1:
		st = st.lower()
		dict1[st] = dict1.get(st, 0) + 1
	
	for st in str2:
		st = st.lower()
		dict2[st] = dict2.get(st, 0) + 1
	
	isAnagram = True
	for key in dict1.keys():
		if dict1.get(key, 0) != dict2.get(key, 0):
			isAnagram = False
			break
	
	return isAnagram


class Test(unittest.TestCase):
	def test_two_lists_with_no_intersection (self):
		str1 = "Mary"
		str2 = "Army"
		actual = is_anagram(str1, str2)
		expected = True
		self.assertEqual(actual, expected)
		

unittest.main(verbosity=2)   



    
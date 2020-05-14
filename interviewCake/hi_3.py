import unittest

def highest_product_of_3(list_of_ints):
	if len(list_of_ints) < 3:
		assertRaises

	mx = max(list_of_ints)
	mn = min(list_of_ints)
	max_list = [mn,mn,mn]
	min_list = [mx,mx]

	for i in range(len(list_of_ints)):
		num = list_of_ints[i]
		# check in max_list
		for j in range(len(max_list)):
			if num > max_list[j]:
				max_list[j] = num
				max_list.sort()
				break

		for j in range(len(min_list)):
			if num < min_list[j]:
				min_list[j] = num
				min_list.sort()
				break
	
	m_mx = 1
	for i in range(len(max_list)):
		m_mx = m_mx * max_list[i]

	m_mn = max_list[2]
	for i in range(len(min_list)):
		m_mn = m_mn * min_list[i]

	return max(m_mn, m_mx)



# # highest_product_of_3([1, 2, 3, 4])
# # highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
# # highest_product_of_3([-10, 1, 3, 2, -10])
# highest_product_of_3([-5, -1, -3, -2])

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])

unittest.main(verbosity=2)
import unittest

def two_sum(nums, goal):
    dict = {}
    for i in range(len(nums)):
      diff = goal - nums[i]
      abs_diff = abs(diff)
      if dict.get(diff, -1) == -1:
        # not found 
        dict[nums[i]] = i
      else:
        return [dict[diff], i]

    return []


class Test(unittest.TestCase):

    def test_short_list_sorted(self):
        actual = two_sum([1, 2, 3, 4], 5)
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_longer_list_unsorted(self):
        actual = two_sum([6, 1, 3, 5, 7, 8, 2], 9)
        expected = [0, 2]
        self.assertEqual(actual, expected)

    # def test_list_has_one_negative(self):
    #     actual = two_sum([-5, 4, 8, 2, 3])
    #     expected = 96
    #     self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = two_sum([-10, 1, 3, 2, 9], -1)
        expected = [0, 4]
        self.assertEqual(actual, expected)

    # def test_list_is_all_negatives(self):
    #     actual = two_sum([-5, -1, -3, -2])
    #     expected = -6
    #     self.assertEqual(actual, expected)

    # def test_error_with_empty_list(self):
    #     with self.assertRaises(Exception):
    #         two_sum([])

    # def test_error_with_one_number(self):
    #     with self.assertRaises(Exception):
    #         two_sum([1])

    # def test_error_with_two_numbers(self):
    #     with self.assertRaises(Exception):
    #         two_sum([1, 1])
  
unittest.main(verbosity=2)

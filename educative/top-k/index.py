# from heapq import *

# def find_k_largest_numbers(nums, k):
#     return nlargest(k, nums)

# def main():

#     print("Here are the top K numbers: " +
#             str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

#     print("Here are the top K numbers: " +
#             str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))

# main()

#    .   


#!/usr/bin/env python3
import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
   	    expected = "breee@abc.edu"
   	    self.assertEqual(find_email(testcase), expected)
	
    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
    unittest.main()
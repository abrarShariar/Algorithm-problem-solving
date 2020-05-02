import unittest

# without using separate list in place
def sort_scores (unsorted_scores, highest_possible_score):
    dict = {}
    for score in unsorted_scores:
        dict[score] = dict.get(score, 0) + 1 
    
    list_index = 0
    for num in range(highest_possible_score, -1 , -1):
        rep = dict.get(num, 0)
        for i in range(rep):
            unsorted_scores[list_index] = num
            list_index += 1
        if list_index >= len(unsorted_scores):
            break
    return unsorted_scores

# using a dict and result list O(n) space 
# def sort_scores(unsorted_scores, highest_possible_score):

#     # Sort the scores in O(n) time
#     dict = {}
#     result = []
#     for score in unsorted_scores:
#         dict[score] = dict.get(score, 0) + 1
    
#     for num in range(highest_possible_score, -1, -1):
#         result += [num] * dict.get(num, 0)
    
#     return result

# Tests
class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
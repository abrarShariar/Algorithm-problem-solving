
# Official solution

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):
        current_price = stock_prices[i]
        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit

# my solution
# def get_max_profit(stock_prices):

#     min_buying = stock_prices[0]
#     max_selling = stock_prices[1]
#     max_profit = max_selling - min_buying

#     # O(n) time
#     for i in range(len(stock_prices)-1):
#         current_buying = stock_prices[i]
#         current_selling = stock_prices[i+1]

#         if current_buying < min_buying:
#             min_buying = current_buying
#             max_selling = current_selling
#         if current_selling > max_selling:
#             max_selling = current_selling

#         max_profit = max(max_profit, max_selling - min_buying)
    
#     return max_profit

# Tests
import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
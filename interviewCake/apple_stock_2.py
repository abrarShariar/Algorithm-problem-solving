def get_max_profit(stock_prices):

    # Calculate the max profit
    buy_index = 0
    sell_index = buy_index + 1
    mx_profit = stock_prices[sell_index] - stock_prices[buy_index]
    # for sell
    for i in range(1,len(stock_prices)):
        if (stock_prices[i] - stock_prices[buy_index]) > mx_profit:
            mx_profit = stock_prices[i] - stock_prices[buy_index]
            sell_index = i

    # for buy
    for i in range(1, sell_index):
        if stock_prices[i] < stock_prices[buy_index]:
            mx_profit = mx_profit + (stock_prices[buy_index] - stock_prices[i])

    return mx_profit


# print(get_max_profit([9, 7, 4, 1]))

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
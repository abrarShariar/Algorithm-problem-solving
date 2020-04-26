import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Check if we're serving orders first-come, first-served
    take_index = 0
    dine_index = 0
    served_index = 0

    while served_index < len(served_orders):
        take_n = take_out_orders[take_index] if take_index < len(take_out_orders) else -1
        dine_n = dine_in_orders[dine_index] if dine_index < len(dine_in_orders) else -1
        serve_n = served_orders[served_index]
        if take_n != -1 and serve_n == take_n:
            take_index += 1
        elif dine_n != -1 and serve_n == dine_n:
            dine_index += 1
        else:
            return False

        served_index += 1

    if served_index < len(served_orders) or take_index < len(take_out_orders) or dine_index < len(dine_in_orders):
        return False

    return True


# print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]))

# Tests
class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)


unittest.main(verbosity=2)

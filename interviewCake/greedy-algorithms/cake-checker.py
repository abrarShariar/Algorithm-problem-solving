import unittest


# MY SOLUTION
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    take_out_index, dine_in_index, current_item_index = 0, 0, 0
    
    while current_item_index < len(served_orders) and take_out_index < len(take_out_orders) and dine_in_index < len(dine_in_orders):
        if served_orders[current_item_index] != take_out_orders[take_out_index] and served_orders[current_item_index] != dine_in_orders[dine_in_index]:
            return False

        elif served_orders[current_item_index] == take_out_orders[take_out_index]:
            take_out_index += 1
         
        elif served_orders[current_item_index] == dine_in_orders[dine_in_index]:
            dine_in_index += 1
        
        current_item_index += 1

    while take_out_index < len(take_out_orders) and current_item_index < len(served_orders):
        if served_orders[current_item_index] != take_out_orders[take_out_index]:
            return False
        
        current_item_index += 1
        take_out_index += 1

    while dine_in_index < len(dine_in_orders) and current_item_index < len(served_orders):
        if served_orders[current_item_index] != dine_in_orders[dine_in_index]:
            return False

        current_item_index += 1
        dine_in_index += 1

    if dine_in_index < len(dine_in_orders) or take_out_index < len(take_out_orders) or current_item_index < len(served_orders):
        return False

    return True

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

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)
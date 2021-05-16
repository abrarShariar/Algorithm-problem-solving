import unittest

def min_changer(money_sum):
    denominations = set([1,3,4])
    min_changes = {}
    min_changes[0] = 0

    for value in denominations:
        min_changes[value] = 1
    
    for current_money in range(1, money_sum + 1):
        

# def min_changer(money_sum):
#     denominations = set([1,3,4])
#     min_changes = {}
#     min_changes[0] = 0
#     # set the value to 1 for denominations, because thats the minimum one
#     for value in denominations:
#         min_changes[value] = 1

#     # start generating the min changes and store in min_changes dunamically
#     for current_money in range(1, money_sum+1):
#         if not (current_money in denominations):
#             min_change_list = []
#             for value in denominations:
#                 if value < current_money:
#                     min_change_list.append(min_changes[value])
            
#             # min_changes[i] = min(min_changes[i-1] + 1, get_greedy(i, denominations))
#             min_changes[current_money] = min(min_changes[current_money-1] + 1, min(min_change_list))

    print(min_changes)
    return min_changes[money_sum]

def get_greedy(money, denominations):
    change_count = 0
    denominations = list(denominations)
    current_denomination_index = len(denominations) - 1
    while money > 0 and current_denomination_index >= 0:
        current_denomination = denominations[current_denomination_index]
        if money < current_denomination:
            current_denomination_index -= 1
            continue
        
        change_count += 1
        money = money - denominations[current_denomination_index]

    return change_count


class TestChangeMethods(unittest.TestCase):
    def test_get_greedy_method(self):
        self.assertEqual(get_greedy(2, set([1,3,4])), 2)
        self.assertEqual(get_greedy(3, set([1,3,4])), 1)
        self.assertEqual(get_greedy(5, set([1,3,4])), 2)

    def test_min_changer_method(self):
        # self.assertEqual(min_changer(34), 9)
        # self.assertEqual(min_changer(2), 2)

if __name__ == '__main__':
    unittest.main()
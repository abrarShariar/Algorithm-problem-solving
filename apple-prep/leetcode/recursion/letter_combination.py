class Solution:
    def letterCombinations(self, digits):
        digit_to_letters = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        available_letters_list = []
        for digit in digits:
            available_letters_list.append(digit_to_letters[digit])

        result_set = set()
        self.get_all_combinations(available_letters_list, result_set)

    def get_all_combinations(self, available_letters_list):

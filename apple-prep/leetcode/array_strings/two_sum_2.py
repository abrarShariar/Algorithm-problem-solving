# SOLVED!
class Solution:
    def twoSum(self, numbers, target):
        start_pointer, end_pointer = 0, len(numbers) - 1
        while start_pointer < end_pointer:
            current_sum = numbers[start_pointer] + numbers[end_pointer]
            if current_sum == target:
                return [start_pointer+1, end_pointer+1]
            elif current_sum < target:
                start_pointer += 1
            elif current_sum > target:
                end_pointer -= 1


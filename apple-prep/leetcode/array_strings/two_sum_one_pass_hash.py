# SOLVED with one pass!! Whohooooooo
class Solution:
    def twoSum(self, nums, target):
        num_hash_map = {}
        for i in range(len(nums)):
            current_num = nums[i]
            rem_num = target - current_num
            if rem_num in num_hash_map.keys():
                return [i, num_hash_map[rem_num]]

            num_hash_map[current_num] = i
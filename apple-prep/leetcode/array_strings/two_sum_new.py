# SOLVED!
class Solution:
    def twoSum(self, nums, target):
        # create a hash map of the indices
        num_index_map = {}
        for i in range(len(nums)):
            num_index_map[nums[i]] = num_index_map.get(nums[i], []) + [i]

        # loop over and find the corresponding element
        for i in range(len(nums)):
            current_num = nums[i]
            rem_num = target - current_num
            # find the rem number in our hash map
            if rem_num in num_index_map.keys():
                for index in num_index_map[rem_num]:
                    if index != i:
                        return [i, index]

        # this appoarch won't work since we need the indices to be in the input order not the sorted order
        # nums.sort()
        # while start_pointer < end_pointer:
        #     current_sum = nums[start_pointer] + nums[end_pointer]
        #     if current_sum == target:
        #         return [start_pointer, end_pointer]
        #     elif current_sum < target:
        #         start_pointer += 1
        #     else:
        #         end_pointer -= 1





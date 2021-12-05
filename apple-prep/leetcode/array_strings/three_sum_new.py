# SOLVED!
class Solution:
    def threeSum(self, nums):
        start_pointer = 0
        result_list = []
        nums.sort()

        already_added_indices = set()

        while start_pointer < len(nums) - 1:
            running_start_pointer = start_pointer + 1
            running_end_pointer = len(nums) - 1
            target_sum = 0 - nums[start_pointer]
            # apply two sum with 2 pointer here
            while running_start_pointer < running_end_pointer:
                current_sum = nums[running_start_pointer] + nums[running_end_pointer]
                if current_sum == target_sum:
                    if not (nums[start_pointer], nums[running_start_pointer], nums[running_end_pointer]) in already_added_indices:
                        result_list.append([nums[start_pointer], nums[running_start_pointer], nums[running_end_pointer]])
                        already_added_indices.add((nums[start_pointer], nums[running_start_pointer], nums[running_end_pointer]))
                    running_start_pointer += 1
                    running_end_pointer -= 1
                elif current_sum > target_sum:
                    running_end_pointer -= 1
                elif current_sum < target_sum:
                    running_start_pointer += 1

            start_pointer += 1

        return result_list



# # NEEDS to be revised! - NOT SOLVED
# class Solution:
#     def threeSum(self, nums):
#         start_pointer = 0
#         result_list = []
#         while start_pointer < len(nums) - 2:
#             current_sum = nums[start_pointer]
#             target_sum = 0 - current_sum
#             running_start_pointer = start_pointer + 1
#             num_index_map = {}
#
#             # Use the one-pass hash map approach here - no 2 pointer necessary
#             # apply two sum from here
#             while running_start_pointer < len(nums) - 1:
#                 complement_num = target_sum - nums[running_start_pointer]
#                 # check if we have already seen this number
#                 if complement_num in num_index_map.keys():
#                     # find the index that is not the current running start pointer
#                     for index in num_index_map[complement_num]:
#                         if index != running_start_pointer:
#                             result_list.append([nums[start_pointer], nums[running_start_pointer], nums[index]])
#
#                 num_index_map[nums[running_start_pointer]] = num_index_map.get(nums[running_start_pointer], []) + [running_start_pointer]
#                 running_start_pointer += 1
#
#             start_pointer += 1
#
#         return result_list
#
#
#

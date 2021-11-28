# SOLVED!
# https://leetcode.com/problems/two-sum/

# class Solution:
# 	def twoSum(self, nums: List[int], target: int) -> List[int]:
# 		start, end = 0, len(nums) - 1
# 		nums.sort()
# 		while start < end:
# 			current_sum = nums[start] + nums[end]
# 			if current_sum == target:
# 				return [start, end]
# 			elif current_sum < target:
# 				start += 1
# 			elif current_sum > target:
# 				end -= 1

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		# create a hashmap of the indices
		indices_map = {}
		for i in range(len(nums)):
			indices_map[nums[i]] = indices_map.get(nums[i], []) + [i]
		
		# loop over the nums and find the diff's index
		for i in range(len(nums)):
			diff = target - nums[i]
			if diff in indices_map:
				indices_list = indices_map[diff]
				for index in indices_list:
					# if the index and the current item's index is not same
					if index != i:
						return [i, index]
				
		

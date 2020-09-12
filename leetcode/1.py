class Solution:
		def twoSum(self, nums, target):
			dict = {}
			for i in range(len(nums)):
				remain_val = target - nums[i]
				d_index = dict.get(remain_val, -1)
				if d_index != -1:
					return [i, d_index]
				else:
					dict[nums[i]] = i


sol = Solution()
# print(sol.twoSum([3,3], 6))
# print(sol.twoSum([3,4], 6))
# print(sol.twoSum([1,2,3,4], 5))
print(sol.twoSum([0,4,3,0], 0))
print(sol.twoSum([-3,4,3,90], 0))
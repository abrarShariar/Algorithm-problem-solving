class Solution:
		def maxSubArray(self, nums):
			current_streak = nums[0]
			global_streak = nums[0]
			
			for i in range(1, len(nums)):
				# update current streak
				current_streak = max(nums[i], current_streak + nums[i])

				# update global streak
				global_streak = max(global_streak, current_streak)
			
			return global_streak

sol = Solution()
print(sol.maxSubArray([-1, 2, 3, -5, 4]))
				

				
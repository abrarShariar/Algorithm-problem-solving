class Solution:
		def maxSubArray(self, nums):
			current_streak = nums[0]
			global_streak = nums[0]
			
			for i in range(1, len(nums)):
				# update current streak
				if current_streak + nums[i] > nums[i]:
					current_streak = current_streak + nums[i]
				else:
					current_streak = nums[i]

				# update global streak
				if current_streak > global_streak:
					global_streak = current_streak 
			
			return global_streak

sol = Solution()
print(sol.maxSubArray([-1, 2, 3, -5, 4]))
				

				
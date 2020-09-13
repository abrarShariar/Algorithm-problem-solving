class Solution:
		def maxProduct(self, nums):
			current_streak = nums[0]
			global_streak = nums[0]

			for i in range(1, len(nums)):
				current_streak = max(current_streak * nums[i], nums[i])
				global_streak = max(global_streak, current_streak)

			return global_streak

sol = Solution()
print(sol.maxProduct([2,3,-2,4]))
print(sol.maxProduct([-2,0,-1]))

# 24 
print(sol.maxProduct([-2,3,-4]))
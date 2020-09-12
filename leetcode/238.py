class Solution:
		def productExceptSelf(self, nums):
			answer_list = [1]
			for i in range(len(nums) - 1):
				answer_list.append(answer_list[-1] * nums[i])

			runnng_product = 1
			for i in range(len(nums) - 1, -1, -1):
				answer_list[i] = runnng_product * answer_list[i]
				runnng_product = runnng_product * nums[i]

			return answer_list

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
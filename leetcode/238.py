class Solution:
		def productExceptSelf(self, nums):
			front_list = [1]
			for i in range(len(nums)):
				last_inserted_item = front_list[-1]
				front_list.append(nums[i] * last_inserted_item)
			
			# generate the result_list 
			# loop over inversely
			result_list = [None] * len(nums)
			running_product = nums[len(nums) - 1]
			result_list[len(nums) - 1] = front_list[len(nums) - 1]

			for i in range(len(result_list)-2, -1, -1):
				result_list[i] = running_product * front_list[i]
				running_product = running_product * nums[i]
				
			return result_list



sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
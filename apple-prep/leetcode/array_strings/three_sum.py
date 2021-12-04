# NEED to revise - NOT SOLVED
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		start_index = 0
		result_list = []
		# nums_set = set(nums)
		# nums = list(nums)
		nums.sort()
		running_sum_set = set()

		while start_index < len(nums) - 1:
			right_index = len(nums) - 1
			left_index = start_index + 1
			current_sum = nums[start_index]

			while left_index < right_index:
				running_sum = nums[left_index] + nums[right_index]
				if running_sum + current_sum == 0:
					if not (running_sum in running_sum_set):
						result_list.append([nums[start_index], nums[left_index], nums[right_index]])
						running_sum_set.add(running_sum)

					left_index += 1
					right_index -= 1
				elif running_sum + current_sum  < 0:
					left_index += 1
				elif running_sum + current_sum  > 0:
					right_index -= 1
			
			start_index += 1

		return result_list


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))

			
					


# faster than 99%!

class Solution:
	def findDuplicate(self, nums) -> int:
		slow_index = 0
		fast_index = 0
		# find meeting ;point of cycle
		while fast_index < len(nums):
			slow_index = nums[slow_index]
			fast_index = nums[nums[fast_index]]
			if slow_index == fast_index:
				break

		# print(slow_index, fast_index)
		# find starting point of cycle
		if slow_index == fast_index:
			slow_index = 0
			while nums[slow_index] != nums[fast_index]:
				slow_index = nums[slow_index]
				fast_index = nums[fast_index]
			return nums[fast_index]
		else:
			None


x = Solution()
print(x.findDuplicate([1,3,4,2,2]))
print(x.findDuplicate([3,1,3,4,2]))
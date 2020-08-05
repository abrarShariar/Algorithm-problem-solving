# SOLVED

from math import floor

def majorityElement(nums):
		n = len(nums)/2
		count_dict = {}
		
		# set item count to dict
		# O(n)
		for item in nums:
			count_dict[item] = count_dict.get(item, 0) + 1
			
		# O(n)
		# count the number of occurances
		for key in count_dict.keys():
			if count_dict[key] > n:
				return key

		
print(majorityElement([1, 1, 1, 4, 2, 4, 4, 3, 1, 1, 1]))
print(majorityElement([4,2,4]))
def find_permutations(nums):
	result = []
	running_permutations = [[]]

	for i in range(len(nums)):
		current_num = nums[i]
		running_res = []
		
		while len(running_permutations) > 0:
			current_perm = running_permutations.pop()
			current_perm_len = len(current_perm)

			for j in range(current_perm_len + 1):
				temp_current_perm = list(current_perm)
				temp_current_perm.insert(j, current_num)
				running_res.append(temp_current_perm)

		if i == len(nums) - 1:
			result = running_res
			return result
		else:
			running_permutations = running_res

def main():
	print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

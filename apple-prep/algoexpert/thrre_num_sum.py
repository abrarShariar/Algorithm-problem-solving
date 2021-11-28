# PASSED
# https://www.algoexpert.io/questions/Three%20Number%20Sum

def threeNumberSum(array, targetSum):
	current_pointer = 0
	result_list = []
	
	array.sort()
	while current_pointer < len(array) - 1:
		current_num = array[current_pointer]
		start_pointer = current_pointer + 1
		end_pointer = len(array) - 1

		while start_pointer < end_pointer:
			running_sum = array[current_pointer] + array[start_pointer] + array[end_pointer]
			if running_sum == targetSum:
				result_list.append([array[current_pointer], array[start_pointer], array[end_pointer]])
				start_pointer += 1
				end_pointer -= 1
			elif running_sum > targetSum:
				end_pointer -= 1
			elif running_sum < targetSum:
				start_pointer += 1

		current_pointer += 1		
	
	return result_list

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
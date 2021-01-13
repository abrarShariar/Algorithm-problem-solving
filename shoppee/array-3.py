# Merge two sorted arrays, unique elements
def merge_sorted_arr(a1, a2):
	a1_index, a2_index = 0, 0
	result_arr = []

	while a1_index < len(a1) and a2_index < len(a2):
		current_min = 0
		if a1[a1_index] < a2[a2_index]:
			current_min = a1[a1_index]
			a1_index += 1
		else:
			current_min = a2[a2_index]
			a2_index += 1
		
		if len(result_arr) > 0 and result_arr[-1] == current_min:
			continue
		
		result_arr.append(current_min)

	# append the remaining items
	while a1_index < len(a1):
		result_arr.append(a1[a1_index])
		a1_index += 1
	
	while a2_index < len(a2):
		result_arr.append(a2[a2_index])
		a2_index += 1
	
	return result_arr


if __name__ == '__main__':
	print(merge_sorted_arr([1,2,3,5, 10], [1,3,4,5,100]))
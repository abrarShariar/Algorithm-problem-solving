def find_item(target_num, input_list, result_list, running_indices):
	# loop over all the items in the list
	for index in range(len(input_list)):
		if isinstance(input_list[index], list):
			running_indices.append(index)
			return find_item(target_num, input_list[index], result_list, running_indices)
		else:
			# loop over all items
			if input_list[index] == target_num:
				running_indices.append(index)
		
	result_list.append(running_indices)
	running_indices = []
	return result_list

input_list = [
	[
		[1,2,3], [2]
	]
]

input_list2 = [1,2,3,4,5,6,7,8,9,2]

print(find_item(2, input_list2, [], []))

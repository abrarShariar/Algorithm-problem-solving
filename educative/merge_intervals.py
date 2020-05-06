def merge_interval(interval_list):
	interval_list.sort(key = lambda x: x[0])
	start, end = interval_list[0][0], interval_list[0][1]
	result_list = []
	for i in range(1, len(interval_list)):
		current_start = interval_list[i][0]
		current_end = interval_list[i][1]
		if current_start <= end:
			end = max(current_end, end)
		else:
			result_list.append([start, end])
			start = current_start
			end = current_end

	result_list.append([start, end])

	return result_list

	
	# while current_index < len(interval_list):
	# 	c_start = interval_list[current_index][0]
	# 	c_end = interval_list[current_index][1]

	# 	print(c_start)
	# 	print(c_end)
	# 	print(result_index)

	# 	if result_index == 0:
	# 		l_start = interval_list[current_index - 1][0]
	# 		l_end = interval_list[current_index - 1][1]
	# 	else:
	# 		l_start = result[result_index - 1][0]
	# 		l_end = result[result_index - 1][1]

	# 	if c_start >= l_start and c_start <= l_end:
	# 		result[result_index] = [l_start, max(c_end, l_end)]
	# 		result_index += 1
	# 	else:
	# 		result.append([c_start, c_end])
	# 		result_index += 1

	# 	current_index += 1

	# return result


print(merge_interval([[1,4], [2,5], [7,9]]))
print(merge_interval([[1,4], [2,6], [3,5]]))
		



def merge_interval(interval_list):
	interval_list.sort(key = lambda x: x[0])
	current_index = 1
	result = [[0,0]]
	print(result)
	result_index = 0
	
	while current_index < len(interval_list):
		c_start = interval_list[current_index][0]
		c_end = interval_list[current_index][1]

		print(c_start)
		print(c_end)
		print(result_index)

		if result_index == 0:
			l_start = interval_list[current_index - 1][0]
			l_end = interval_list[current_index - 1][1]
		else:
			l_start = result[result_index - 1][0]
			l_end = result[result_index - 1][1]

		if c_start >= l_start and c_start <= l_end:
			result[result_index] = [l_start, max(c_end, l_end)]
			result_index += 1
		else:
			result.append([c_start, c_end])
			result_index += 1

		current_index += 1

	return result


print(merge_interval([[1,4], [2,5], [7,9]]))
print(merge_interval([[1,4], [2,6], [3,5]]))
		



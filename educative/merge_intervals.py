# def merge_interval(interval_list):
# 	interval_list.sort(key = lambda x: x[0])
# 	current_index = 1
# 	result = [interval_list[0][0], interval_list[0][1]]
# 	result_index = 0
	
# 	while current_index < len(interval_list):
# 		c_start = interval_list[current_index][0]
# 		c_end = interval_list[current_index][1]
		
# 		l_start = result[result_index][0]
# 		l_end = result[result_index][1]

# 		if interval_list[current_index][0] >= interval_list[prev][0] and interval_list[current_index][0] <= interval_list[prev][1]:
			
# 			result[result_index] = [interval_list[prev][0], max(interval_list[current_index][1], interval_list[current_index][1])]
# 			result_index += 1

# 		current += 1

# 	return result


# print(merge_interval([[1,4], [2,5], [7,9]]))
		



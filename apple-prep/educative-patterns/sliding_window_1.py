def max_sub_array_of_size_k(k, input_array):
	running_sum = 0
	max_sum = 0
	start = 0
	end = start
	
	if end >= len(input_array):
		print("The number oof elemments to sum: K is out of bounds!")
		return None

	while end < len(input_array):
		if end > k - 1:
			running_sum -= input_array[start]
			start += 1

		running_sum += input_array[end]
		end += 1
		max_sum = max(running_sum, max_sum)
	
	return max_sum


print(get_max_from_sub_array(input_array = [2, 1, 5, 1, 3, 2], k = 3))

def length_of_longest_substring(arr, k):
	window_start = 0
	max_length = 0
	one_count = 0

	for window_end in range(len(arr)):
		right_digit = arr[window_end]
		if right_digit == 1:
			one_count += 1
		
		current_length = (window_end - window_start) + 1

		# current_length - max_repeated_num = the non reapeated digits or the digits that need to be replaced
		if current_length - one_count > k:
			left_digit = arr[window_start]
			if left_digit == 1:
				one_count -= 1
			
			window_start += 1
			current_length = (window_end - window_start) + 1

		max_length = max(max_length, current_length)

	return max_length
		
print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

		

  

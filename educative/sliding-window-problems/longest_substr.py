# SOLVED
def longest_substring_with_k_distinct(str, k):
	# 1. start the window with first index
	#  - keep track of unique chars in a dictionary
	#  - keep track of the count
	# 2. start expanding the window till we have k keys in dictionary
	#  - keep a running sum
	#  - update the running sum with the max

	char_dict = {}
	running_len = 0
	max_len = 0
	window_start = 0
	
	for window_end in range(len(str)):
		current_char = str[window_end]
		char_dict[current_char] = char_dict.get(current_char, 0) + 1
		running_len += 1

		while len(char_dict) > k:
			# squeeze the window
			# remove the element from window start from  char dict
			# decrease running_len
			char_dict[str[window_start]] = char_dict.get(window_start, 0) - 1
			if char_dict[str[window_start]] <= 0:
				char_dict.pop(str[window_start], None)
			
			running_len -= 1
			window_start += 1
		
		max_len = max(max_len, running_len)
		
	return max_len
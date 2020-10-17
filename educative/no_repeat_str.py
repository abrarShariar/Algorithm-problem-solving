def non_repeat_substring (str):
	window_start = 0
	char_dict = {}
	global_max_len = 0

	for window_end in range(len(str)):
		ch = str[window_end]

		if ch in char_dict:
			window_start = max(window_start, char_dict[ch] + 1)
		
		# if not in dict
		char_dict[ch] = window_end
		global_max_len = max(global_max_len, window_end - window_start + 1)

	return global_max_len

		


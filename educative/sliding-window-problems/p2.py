def find_string_anagrams(str, pattern):
	result_indexes = []
	pattern_freq = {}
	
	window_start, matched = 0, 0

	# create the pattern dictionary
	for char in pattern:
		pattern_freq[char] = pattern_freq.get(char, 0) + 1

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in pattern_freq:
			pattern_freq[right_char] -= 1
			
			if pattern_freq[right_char] == 0:
				matched += 1
		
		if matched == len(pattern):
			result_indexes.append(window_start)

		if window_end >= len(pattern) - 1:
			left_char = str[window_start]

			if left_char in pattern_freq:
				pattern_freq[left_char] += 1
				if pattern_freq[left_char] == 0:
					matched -= 1

			window_start += 1

	return result_indexes
			
# SOLVED
def find_string_anagrams(str, pattern):
	result_indexes = []
	matched, window_start = 0, 0

	pattern_dict = {}

	for ch in pattern:
		pattern_dict[ch] = pattern_dict.get(ch, 0) + 1

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in pattern_dict:
			pattern_dict[right_char] -= 1

			if pattern_dict[right_char] == 0:
				matched += 1
		
		if matched == len(pattern_dict):
			result_indexes.append(window_start)
			
		# shrink the window
		if window_end >= len(pattern) - 1:
			left_char = str[window_start]
			if left_char in pattern_dict:
				if pattern_dict[left_char] == 0:
					matched -= 1

				pattern_dict[left_char] += 1
			
			window_start += 1

	return result_indexes

print(find_string_anagrams("pppsqp", "pq"))
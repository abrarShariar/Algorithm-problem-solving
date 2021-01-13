def find_substring(str, pattern):
	window_start, matched = 0, 0
	pattern_dict = {}

	# patttern dictionary
	for char in pattern:
		pattern_dict[char] = pattern_dict.get(char, 0) + 1

	
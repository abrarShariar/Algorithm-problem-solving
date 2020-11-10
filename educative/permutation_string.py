def find_permutation(str, pattern):
	# make a dictionary out of pattern
	pattern_dict = {}
	for char in pattern:
		pattern_dict[char] = pattern_dict.get(char, 0) + 1
	
	window_start, matched = 0, 0

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in pattern_dict:
			pattern_dict[right_char] -= 1
			if pattern_dict[right_char] == 0:
				matched += 1

		if matched == len(pattern_dict):
			return True

		if window_end >= len(pattern) - 1:
			left_char = str[window_start]
			
			if left_char in pattern_dict:
				if pattern_dict[left_char] == 0:
					matched -= 1
				
				pattern_dict[left_char] = pattern_dict[left_char] + 1

			window_start += 1
			
	return False

print(find_permutation("oidbcaf", "abc"))
print(find_permutation("odicf", "dc"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))



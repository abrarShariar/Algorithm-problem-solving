def find_permutation(str, pattern):
	# make dictionary of the frequency of the chars from the pattern
	pattern_freq = {}
	for ch in pattern:
		pattern_freq[ch] = pattern_freq.get(ch, 0) + 1

	# initialize variables
	window_start, matched = 0, 0

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in pattern_freq:
			pattern_freq[right_char] -= 1
			matched += 1

		if matched == len(pattern):
			return True
		
		if window_end >= len(pattern) - 1:
			left_char = str[window_start]

			if left_char in pattern_freq:
				pattern_freq[left_char] += 1
				matched -= 1

			window_start += 1
			
	return False

print(find_permutation("oidbcaf", "abc"))
print(find_permutation("odicf", "dc"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))
print(find_permutation("aaacb", "abc"))
# SOLVED

def find_permutation(str, pattern):
	pattern_dict = {x: 1 for x in pattern}
	window_start = 0

	# outer loop => O(str.length)
	for window_end in range(len(str)):
		window_start = window_end
		pattern_length = 0

		# inner loop => O(pattern.length) 
		while pattern_dict.get(str[window_start], 0):
			pattern_length += 1
			if pattern_length == len(pattern):
				return True
			window_start += 1
		
	return False

print(find_permutation("oidbcaf", "abc"))
print(find_permutation("odicf", "dc"))


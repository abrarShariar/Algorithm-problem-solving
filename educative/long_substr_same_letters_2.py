# SOLVED
# PROBLEM LINK: https://www.educative.io/courses/grokking-the-coding-interview/R8DVgjq78yR


def length_of_longest_substring(str, k):
	window_start = 0
	freq_dict = {}
	max_length = 0
	max_repeated_count = 0

	for window_end in range(len(str)):
		right_char = str[window_end]
		freq_dict[right_char] = freq_dict.get(right_char, 0) + 1
		max_repeated_count = max(max_repeated_count, freq_dict[right_char]) 

		current_length = (window_end - window_start) + 1

		if current_length - max_repeated_count > k:
			left_char = str[window_start]
			freq_dict[left_char] -= 1
			window_start += 1
			current_length = (window_end - window_start) + 1
		
		max_length = max(max_length, current_length)

	return max_length


print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))
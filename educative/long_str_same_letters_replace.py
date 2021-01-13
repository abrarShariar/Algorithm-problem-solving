def length_of_longest_substring(str, k):
	window_start = 0
	window_end = window_start

	while window_end < len(str):
		current_char = str[window_start]
		mx_len = 0
		rem_replace = k
		
		for i in range(window_start, len(str)):
			if str[i] != current_char:
				rem_replace -= 1

			if rem_replace <= 0:
				window_end = i + 1
				break

		mx_len = max(mx_len, window_end - window_start) 
		window_start += 1

	return max(mx_len, window_end - window_start)

print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))




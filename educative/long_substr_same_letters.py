# DOES NOT SOLVE

def length_of_longest_substring(str, k):
	if len(str) <= 1:
		return 1

	max_len = 1
	start_index = 0
	end_index = start_index + 1
	
	while end_index < len(str):
		
		current_element = str[start_index]
		temp_k = k
		first_change_index = -1

		while temp_k >= 0 and end_index < len(str):
			if str[end_index] != current_element:
				temp_k -= 1
				if first_change_index == -1:
					first_change_index = end_index

			if end_index >= len(str):
				return max_len

			end_index += 1

		max_len = max(max_len, end_index - start_index)
		if end_index >= len(str):
			return max_len

		start_index = first_change_index
		end_index = start_index + 1

	return max_len

print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abccde", 1))


			
  

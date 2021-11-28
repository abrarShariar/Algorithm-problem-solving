# SOLVED!
def longest_substring_with_k_distinct(str1, k):
	start, end = 0, 0
	max_len = 0
	st_dict = {}

	# O(n)
	while end < len(str1):
		st_dict[str1[end]] = st_dict.get(str1[end], 0) + 1
		# if we have more than K elements - roll back NOW
		# O(N)
		while (len(st_dict.keys()) > k and start < end):
			st_dict[str1[start]] -= 1
			if st_dict[str1[start]] == 0:
				del st_dict[str1[start]]
			
			start += 1
		
		max_len = max(max_len, (end - start) + 1)
		end += 1

	return max_len


# print(longest_substring_with_k_distinct("araaci", 2))
print(longest_substring_with_k_distinct("aracci", 1))
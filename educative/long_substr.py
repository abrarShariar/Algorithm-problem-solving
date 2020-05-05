# SOLVED

def longest_substring_with_k_distinct(str, k):
	start = 0
	end = 0
	dict = {}
	long_len = 0
	while end < len(str):
		# if len of dict keys is less than k
		dict[str[end]] = dict.get(str[end],0) + 1
		if len(dict) == k:
			long_len = max(long_len, (end-start)+1)

		# if len of dict keys is greater than k
		while len(dict) > k:
			dict[str[start]] = dict.get(str[start], 0) - 1
			if dict[str[end]] <= 0:
				# remove that key
				del dict[str[end]]
			start += 1

		end += 1

	return long_len

print(longest_substring_with_k_distinct('araaci', 2))
print(longest_substring_with_k_distinct('araaci', 1))
		

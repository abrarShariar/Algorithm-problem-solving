# SOLVED

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		char_dict = {}
		start, end = 0, 0
		max_len = 0

		while end < len(s):
			char_dict[s[end]] = char_dict.get(s[end], 0) + 1
			# keep removing from start until we have only one element
			while char_dict[s[end]] > 1 and start < end:
				char_dict[s[start]] = char_dict[s[start]] - 1
				if char_dict[s[start]] == 0:
					del char_dict[s[start]]

				start += 1
			
			end += 1
			max_len = max(max_len, len(char_dict.keys()))
			
		return max_len
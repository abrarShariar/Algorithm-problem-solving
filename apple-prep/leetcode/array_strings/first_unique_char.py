# SOLVED!
class Solution:
    def firstUniqChar(self, s: str):
        char_count_map = {}
        for ch in s:
            char_count_map[ch] = char_count_map.get(ch, 0) + 1

        for key, value in char_count_map.items():
            if value == 1:
                # find the element's index
                for i in range(len(s)):
                    if s[i] == key:
                        return i

        return -1
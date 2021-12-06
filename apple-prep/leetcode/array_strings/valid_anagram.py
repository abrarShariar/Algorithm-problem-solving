class Solution:
    def isAnagram(self, s: str, t: str):
        char_dict = {}
        # O(n)
        for ch in s:
            char_dict[ch] = char_dict.get(ch, 0) + 1

        # O(n)
        for ch in t:
            if not ch in char_dict.keys():
                return False

            char_dict[ch] = char_dict[ch] - 1
            if char_dict[ch] == 0:
                del char_dict[ch]

        # if we have a non-zero key - it's not valid anagram
        for key, value in char_dict.items():
            if value != 0:
                return False

        return True
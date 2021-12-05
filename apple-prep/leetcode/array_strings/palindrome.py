# SOLVED!
class Solution:
    def isPalindrome(self, s: str):
        if s.strip() == "":
            return True
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True

        alphanumeric_set = set()
        for i in range(ord('a'), ord('z') + 1):
            alphanumeric_set.add(chr(i))

        for i in range(ord('0'), ord('9') + 1):
            alphanumeric_set.add(chr(i))

        start_pointer, end_pointer = 0, len(s) - 1
        while start_pointer <= end_pointer:
            start_char = s[start_pointer].lower()
            end_char = s[end_pointer].lower()
            if start_char not in alphanumeric_set:
                start_pointer += 1
                continue
            if end_char not in alphanumeric_set:
                end_pointer -= 1
                continue

            # Both start and end char are alpha num now
            if start_char != end_char:
                return False
            else:
                start_pointer += 1
                end_pointer -= 1

        return True

# sol = Solution()
# print(sol.isPalindrome("0P"))
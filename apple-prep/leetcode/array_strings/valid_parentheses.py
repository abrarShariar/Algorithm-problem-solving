# SOLVED!
class Solution:
    def isValid(self, s):
        if len(s) <= 1:
            return False
        # create stack to push the opening brackets - pop on closing bracket
        opening_bracket_stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # if we have a closing bracket - find the corresponding opening bracket
            if ch in bracket_map.keys():
                if len(opening_bracket_stack) == 0:
                    return False
                while len(opening_bracket_stack) > 0:
                    current_element = opening_bracket_stack.pop()
                    if current_element != bracket_map[ch]:
                        return False
                    else:
                        break
            else:
                opening_bracket_stack.append(ch)

        if len(opening_bracket_stack) > 0:
            return False

        return True

# sol = Solution()
# print(sol.isValid("{[]}"))


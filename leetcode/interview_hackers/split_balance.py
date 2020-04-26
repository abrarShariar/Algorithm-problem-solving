# solved

# O(n) space complexity
# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         l_stack = []
#         r_stack = []
#         st_count = 0
#         for i in range(len(s)):
#             if s[i] == 'L':
#                 if not r_stack:
#                     l_stack.append('L')
#                 else:
#                     r_stack.pop()
#                     if not r_stack:
#                         st_count += 1
#             else:
#                 if not l_stack:
#                     r_stack.append('R')
#                 else:
#                     l_stack.pop()
#                     if not l_stack:
#                         st_count += 1
#         return st_count


# O(1) complexity
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        sp_count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                sp_count += 1
                l_count = 0
                r_count = 0
        return sp_count


x = Solution()
print(x.balancedStringSplit("RLRRLLRLRL"))
print(x.balancedStringSplit("RLLLLRRRLR"))
print(x.balancedStringSplit("LLLLRRRR"))
print(x.balancedStringSplit("RLRRRLLRLL"))

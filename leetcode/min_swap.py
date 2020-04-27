# wrong answer
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_dict = {}
        s_dict = {}
        # populate data in s dict
        for ch in s:
            if ch in s_dict.keys():
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
        
        # populate data in t dict
        for ch in t:
            if ch in t_dict.keys():
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1
        
        # find the missing keys/extra keys on t
        ct = 0
        for key in t:
            if key not in s_dict.keys():
                ct += 1
            else: 
                if s_dict[key] > 0:
                    s_dict[key] -= 1
                else:
                    ct += 1
        return ct


x = Solution()
# print(x.minSteps("leetcode", "practice"))
# print(x.minSteps("bab", "aba"))
# print(x.minSteps("anagram", "mangaar"))
# print(x.minSteps("xxyyzz", "xxyyzz"))
# print(x.minSteps("friend", "family"))

# wrong for this (correct: 18)
print(x.minSteps("gctcxyuluxjuxnsvmomavutrrfb", "qijrjrhqqjxjtprybrzpyfyqtzf"))



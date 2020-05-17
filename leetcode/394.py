# SOLVED
# faster than 7% wtf
class Solution:
    def decodeString(self, s):
        nums_stack = []
        chars_stack = []
        ct = ''
        for i in range(0, len(s)):
            ch = s[i]
            # opening bracket
            if ch == '[':
                nums_stack.append(int(ct)) 
                chars_stack.append(ch)
                ct = ''
            # closing bracket -> loop and form output
            elif ch == ']':
                st_list = []
                n = nums_stack.pop()
                # until we find a opening bracket
                while len(chars_stack) > 0 and chars_stack[-1] != '[':
                    char = chars_stack.pop()
                    st_list.insert(0, char)

                if len(chars_stack) > 0:
                    chars_stack.pop()

                str = "".join(st_list)
                res = str
                for i in range(0, n-1):
                    res += str

                chars_stack.append(res)
            elif ord(ch) >= 48 and ord(ch) <= 57:
                ct += ch
            else:
                chars_stack.append(ch)

        return "".join(chars_stack)

            
x = Solution()
# print(x.decodeString("3[a]2[bc]"))
# print(x.decodeString("3[a2[c]]"))
# print(x.decodeString("2[abc]3[cd]ef"))
print(x.decodeString("100[leetcode]"))
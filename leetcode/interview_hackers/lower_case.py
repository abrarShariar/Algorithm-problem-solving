# solved
class Solution:
    def toLowerCase(self, str: str) -> str:
        ascii_a = ord('a')
        ascii_z = ord('z')
        ascii_A = ord('A')
        ascii_Z = ord('Z')
        result_str = ''
        for ch in str:
            ascii_ch = ord(ch)
            if ascii_ch >= ascii_A and ascii_ch <= ascii_Z:
                result_str += chr(ord(ch) + 32)
            else:
                result_str += ch
        
        return result_str

x = Solution()
print(x.toLowerCase("Hello"))
print(x.toLowerCase("here"))
print(x.toLowerCase("LOVELY"))
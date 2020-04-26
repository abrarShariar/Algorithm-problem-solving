# solved
# O(n) space
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_code = set()
        for word in words:
            code = ''
            for ch in word:
                code += table[ord(ch) - ord('a')]
            unique_code.add(code)
        return len(unique_code)

x = Solution()
print(x.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
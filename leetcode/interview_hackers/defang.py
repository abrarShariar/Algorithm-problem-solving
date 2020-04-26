# solved
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

x = Solution()
print(x.defangIPaddr("255.100.50.0"))
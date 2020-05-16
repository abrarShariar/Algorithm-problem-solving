class Solution:
	# @param A : integer
	# @return a strings
	def findDigitsInBinary(self, A):
		res_int = 0
		i = 1
		while A != 0:
			rem = A%2
			rem = i * rem
			i = i * 10
			res_int += rem
			A = int(A/2)
		return str(res_int)

x = Solution()
print(x.findDigitsInBinary(12))
print(x.findDigitsInBinary(99))

		 
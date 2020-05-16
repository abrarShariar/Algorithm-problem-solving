# solved
import math
class Solution:
	# @param A : integer
	# @return a list of integers
	def allFactors(self, A):
		result = []
		for i in range(int(math.sqrt(A)), 0, -1):
			if A%i == 0:
				result.insert(0,i)
				if not i == int(A/i):
					result.append(int(A/i))
				
		return result

x = Solution()
print(x.allFactors(12))
print(x.allFactors(182))
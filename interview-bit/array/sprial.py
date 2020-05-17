class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
		n_rows = len(A)
		n_cols = len(A[0])
		low_i = 0
		hg_i = n_rows
		low_j = 0
		hg_j = n_cols
		result = []

		while hg_i > 0 and hg_j > 0:
			# left -> right
			for j in range(low_j, hg_i):
				if A[low_i][j] != 0:
					# print(A[low_i][j])
					result.append(A[low_i][j])
				A[low_i][j] = 0

			# top -> down
			for i in range(low_i + 1, hg_i):
				if A[i][hg_j - 1] != 0:
					# print(A[i][hg_j - 1])
					result.append(A[i][hg_j - 1])
				A[i][hg_j - 1] = 0
			
			# left -> right
			for j in range(hg_j - 1, low_j, -1):
				if A[hg_i - 1][j] != 0:
					# print(A[hg_i - 1][j])
					result.append(A[hg_i - 1][j])
				A[hg_i - 1][j] = 0
			
			# botton -> up
			for i in range(hg_i - 1, low_i, -1):
				if A[i][low_j] != 0:
					# print(A[i][low_j])
					result.append(A[i][low_j])
				A[i][low_j] = 0
			
			low_i += 1
			low_j += 1
			hg_i -= 1
			hg_j -= 1

		return result


input_list = [
	[1,2,3,4],
	[12,13,14,5],
	[11,16,15,6],
	[10,9,8,7]
]
x = Solution()
print(x.spiralOrder(input_list))
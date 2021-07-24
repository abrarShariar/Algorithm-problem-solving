# SOLVED
def lcs3(a, b, c):
	limit_i = len(a) + 1
	limit_j = len(b) + 1
	limit_k = len(c) + 1

	edit_distance_matrix = [[[[0] for i in range(limit_i)] for j in range(limit_j)] for k in range(limit_k)]

	for k in range(limit_k):
		for j in range(limit_j):
			for i in range(limit_i):
				if i == 0 or j == 0 or k == 0:
					edit_distance_matrix[k][j][i] = 0
				else:
					if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
						edit_distance_matrix[k][j][i] = edit_distance_matrix[k-1][j-1][i-1] + 1
					else:
						edit_distance_matrix[k][j][i] = max(
							edit_distance_matrix[k][j][i-1],
							edit_distance_matrix[k][j-1][i],
							edit_distance_matrix[k-1][j][i]
						)

	return edit_distance_matrix[limit_k-1][limit_j-1][limit_i-1]

print(lcs3([1,2,3], [1,2], [1,2]))				 
				
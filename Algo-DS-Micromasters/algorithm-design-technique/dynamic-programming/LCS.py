#Uses python3
import sys

def lcs2(a, b):

	row = len(a) + 1
	col = len(b) + 1
	
	edit_distance_matrix = [[0 for i in range(col)] for j in range(row)]
	
	for i in range(row):
		for j in range(col):
			if i == 0:
				edit_distance_matrix[i][j] = 0
			elif j == 0:
				edit_distance_matrix[i][j] = 0
			else:
				# if the str1 and str2 has the same values => point is 1
				if a[i-1] == b[j-1]:
					edit_distance_matrix[i][j] = edit_distance_matrix[i-1][j-1] + 1 
				else:
					# find the min and assign
					max_distance = max(
						edit_distance_matrix[i][j-1],
						edit_distance_matrix[i-1][j]
					)
					edit_distance_matrix[i][j] = max_distance
	
	return edit_distance_matrix[len(a)][len(b)]
	
print(lcs2([1],[10]))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))

#     n = data[0]
#     data = data[1:]
#     a = data[:n]

#     data = data[n:]
#     m = data[0]
#     data = data[1:]
#     b = data[:m]

#     print(lcs2(a, b))

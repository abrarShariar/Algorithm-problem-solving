# SOLVED
def edit_distance_matrix(str1, str2):
	row = len(str1) + 1
	col = len(str2) + 1
	
	edit_distance_matrix = [[0 for i in range(col)] for j in range(row)]
	
	for i in range(row):
		for j in range(col):
			if i == 0:
				edit_distance_matrix[i][j] = j
			elif j == 0:
				edit_distance_matrix[i][j] = i
			else:
				# if the str1 and str2 has the same values => point is 1
				if str1[i-1] == str2[j-1]:
					edit_distance_matrix[i][j] = edit_distance_matrix[i-1][j-1] 
				else:
					# find the min and assign
					min_distance = min(
						edit_distance_matrix[i][j-1] + 1,
						edit_distance_matrix[i-1][j] + 1,
						edit_distance_matrix[i-1][j-1] + 1
					)
					edit_distance_matrix[i][j] = min_distance
	
	return edit_distance_matrix[len(str1)][len(str2)]

# result_matrix = edit_distance_matrix('ME', 'EDIT')
# result_matrix = edit_distance_matrix('CAT', 'CAT')
str1 = input()
str2 = input()

result = edit_distance_matrix(str1, str2)

# the last index should give the desired min index
print(result)

# WRONG:
# def edit_distance(str1, str2):
# 	str1_len = len(str1)
# 	str2_len = len(str2)

# 	# edit
# 	edit_distance_matrix = [[0] * (str1_len + 1)] * (str2_len + 1)

# 	# str1 = column
# 	# str2 = row

# 	# initizlize
# 	for i in range(len(edit_distance_matrix)):
# 		for j in range(len(edit_distance_matrix[0])):
# 			if i == 0:
# 				edit_distance_matrix[i][j] = 999

# 	return edit_distance_matrix

# result = edit_distance('edit', 'me')
# # print(result)

# mat = [
# 	[0,0,0,0],
# 	[0,0,0,0]
# ]

# col = 4
# row = 2
# mat = [
#  [0, 0, 0, 0],
#  [0, 0, 0, 0]
# ]

# print(mat)

# for i in range(len(mat)):
# 	for j in range(len(mat[0])):
# 		if i == 0:
# 			print(i, j)
# 			mat[i][j] = 999

# print(mat)


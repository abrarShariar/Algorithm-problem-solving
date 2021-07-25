# tutorial: https://www.youtube.com/watch?v=xCbYmUPvc2Q
# 0/1 Knapsack 

def do_knapsack(max_weight, item_weights, item_values):
	row = len(item_values) + 1
	col = max_weight + 1

	# initialize the values matrix
	# this will hold all our previous computations - DP way
	values_matrix = [[0 for i in range(col)] for j in range(row)]
	# loop over and populate the matrix 
	# the fun begin here!
	for i in range(1, row): 
		for j in range(0, col):
			item_value = item_values[i - 1]
			item_weight = item_weights[i - 1]
			current_max_weight = j
			# check if the current_max_weight is less the allowed max weight
			if item_weight <= current_max_weight:
				# take the max of the two options:
					# value of (the previous item + same weight)
					# value of (the previous item + whatever remains after removing the current item weight) + current item's value
				values_matrix[i][j] = max (
					values_matrix[i-1][current_max_weight],
					values_matrix[i-1][current_max_weight - item_weight] + item_value
				)
			else:
				# we cannot take any value for this item so assign the previous item's weight 
				values_matrix[i][j] = values_matrix[i-1][j]

	# the last cell is the answer
	return values_matrix[len(values_matrix) - 1][len(values_matrix[0]) - 1]

max_weight = 5
item_weights = [5, 3, 4, 2]
item_values = [60, 50, 70, 30]
print(do_knapsack(max_weight, item_weights, item_values))


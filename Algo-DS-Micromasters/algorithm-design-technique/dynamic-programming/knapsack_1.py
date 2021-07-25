def knap(total_weight, input_values, input_weights):
	values_list = [0 for w in range(total_weight + 1)]
	total_input_items = len(input_values)

	# we are increasing the size of the knapsack
	for w in range(1, total_weight + 1):
		# initialize 
		values_list[w] = 0
		# loop over all the items in the list
		for i in range(0, total_input_items):
			if input_weights[i] <= w:
				val = values_list[w - input_weights[i]] + input_values[i]
				if val > values_list[w]:
					values_list[w] = val

	print(values_list)
	return values_list[total_weight]					
	

input_weights = [
	6, 3, 4, 2
]

input_values = [
	30, 14, 4, 2
]

knapsack_total_weight = 10

knap(knapsack_total_weight, input_values, input_weights)

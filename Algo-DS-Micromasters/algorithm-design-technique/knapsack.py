def knapsack(items, maxSize):
	unit_dict = {}
	knapsack = []

	# calculate per unit cost
	for (weight, value) in items:
		unit_price = int(value/weight)
		unit_dict[unit_price] = weight

	# sort based on unit cost
	sorted_unit = sorted(unit_dict, reverse=True)
	sorted_unit_index = 0

	while sorted_unit_index < len(sorted_unit) and maxSize > 0:
		unit_price = sorted_unit[sorted_unit_index]
		item_weight = unit_dict[unit_price]

		if maxSize - item_weight >= 0:
			knapsack.append(item_weight)
			maxSize = maxSize - item_weight

		sorted_unit_index += 1
	
	print(maxSize)
	
	return knapsack

weight_value_input = [(5, 30), (4, 28), (3, 24)]
print(knapsack(weight_value_input, 9))



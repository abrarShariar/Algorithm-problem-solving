def fruits_into_baskets(fruits):
	hash_map = {}
	running_max = 0
	window_start = 0

	for i in range(len(fruits)):
		current_fruit_tree = fruits[i]
		# if hash_map keys len is greater than 2, move

		if len(hash_map.keys()) == 2 and hash_map.get(current_fruit_tree, -1) == -1:
			outgoing_item = fruits[window_start]
			hash_map[outgoing_item] = hash_map.get(outgoing_item, 0) - 1
			
			if hash_map[outgoing_item] == 0:
				del hash_map[outgoing_item]

			window_start += 1
	
		hash_map[current_fruit_tree] = hash_map.get(current_fruit_tree, 0) + 1

	sum = 0	
	for key in hash_map.keys():
		sum += hash_map[key]

	return sum

print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
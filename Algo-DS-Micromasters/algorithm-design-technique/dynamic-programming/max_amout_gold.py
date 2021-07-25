def optimal_weight(W, w):
	# write your code here
	result = 0
	# sort the w in desc order
	w.sort(reverse=True)
	for x in w:
		if result + x <= W:
			result = result + x

	return result

print(optimal_weight(10, [1,4,8]))

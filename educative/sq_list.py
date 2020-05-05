def sq_list(arr):
	left = 0
	right = len(arr) - 1
	result = []
	while left < right:
		left_sq = arr[left] ** 2
		right_sq = arr[right] ** 2
		if left_sq >= right_sq:
			result.insert(0, left_sq)
			left += 1
		else:
			result.insert(0, right_sq)
			right -= 1
		
	result.insert(0, arr[left]**2)
	return result

print(sq_list([-2,-1,0,2,3]))
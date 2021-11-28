def pair_with_targetsum(arr, target_sum):
	start, end = 0, len(arr) - 1
	while start < end:
		sum = arr[start] + arr[end]
		if sum == target_sum:
			return [start, end]
		elif sum > target_sum:
			end -= 1
		else:
			start += 1
			
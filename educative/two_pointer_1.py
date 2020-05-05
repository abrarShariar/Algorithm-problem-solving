def pair_with_targetsum(arr, target_sum):
	start = 0
	end = len(arr) - 1
	sum = 0
	while start < end:
		sum = arr[start] + arr[end]
		if sum > target_sum:
			end -= 1
		elif sum < target_sum:
			start += 1
		else:
			return [start, end]


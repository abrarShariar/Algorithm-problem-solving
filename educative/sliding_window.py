def find_avg(arr, K):
	start = 0
	end = K - 1
	sum = 0
	result = []
	while end < len(arr):
		# this is the starting index so loop for K
		if start == 0:
			for i in range(0, K):
				sum += arr[i]
		else:
		# if not the first loop, use SUM, no LOOP
			sum -= arr[start-1]
			sum += arr[end]
		
		result.append(sum/K)
		start += 1
		end += 1

	return result

print(find_avg([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


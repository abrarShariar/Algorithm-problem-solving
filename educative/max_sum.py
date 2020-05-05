def max_sub_array_of_size_k (k, arr):
	sum, mx_sum, start = 0, 0, 0
	end = k - 1

	while end < len(arr):
		if start == 0:
			for i in range(k):
				sum += arr[i]
		else:
			sum += arr[end]
			sum -= arr[start - 1]

		mx_sum = max(sum, mx_sum)
		start += 1
		end += 1

	return mx_sum


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
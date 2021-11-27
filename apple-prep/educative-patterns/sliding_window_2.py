def smallest_subarray_with_given_sum(s, arr):
	start, end, running_sum, min_len = 0, 0, 0, len(arr)
	
	while end < len(arr):
		running_sum += arr[end]
		if running_sum >= s:
			min_len = min(min_len, (end - start) + 1)
			# now we should start rolling back
			while start <= end:
				if running_sum < s:
					break

				min_len = min(min_len, (end-start) + 1)
				running_sum -= arr[start]
				start += 1

			start = end
			running_sum = arr[start]

		end += 1
	
	return min_len

print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))


# SOLVED - SLIDING WINDOW
def smallest_subarray_with_given_sum(s, arr):
	start = 0
	end = 0
	sum = 0
	min_len = len(arr)
	while end < len(arr):
		while sum < s:
			sum += arr[end]
			end += 1
		while sum >= s:
			min_len = min(min_len, (end - start))
			sum -= arr[start]
			start += 1
		
	return min_len
	
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))

# def smallest_subarray_with_given_sum(s, arr):
# 	start = 0
# 	end = 0
# 	sum = 0
# 	min_len = len(arr)
# 	while end < len(arr) and start < len(arr):
# 		if sum >= s:
# 			min_len = min(min_len, (end - start)+1)
# 			sum -= arr[start]
# 			start += 1
# 		if sum < s:
# 			end += 1
# 			if end >= len(arr):
# 				break
# 			sum += arr[end]
	
# 	return min_len


# # print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
# # print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))

# print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))

  

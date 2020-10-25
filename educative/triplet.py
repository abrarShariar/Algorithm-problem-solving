def search_triplets(arr):
	triplets = []

	# sort the input arr
	arr.sort()

	for i in range(len(arr)):
		target = arr[i]
		# use two pointers 
		start = i + 1
		end = len(arr) - 1
		while start < end:
			sum = arr[start] + arr[end]
			if sum + target == 0:
				triplets.append([arr[i], arr[start], arr[end]])
				start += 1
				end -= 1
			elif sum + target < 0:
				start += 1
			elif sum + target > 0:
				end -= 1

	return triplets

print(search_triplets([-5, 2, -1, -2, 3]))
print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))

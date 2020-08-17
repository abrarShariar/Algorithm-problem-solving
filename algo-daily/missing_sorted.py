# SOLVED

def missingInUnsorted (arr, lowerbound, upperbound):
	# the theoretical sum
	th_sum = int((upperbound * (upperbound + 1)) / 2)
	current_sum = sum(arr)

	return th_sum - current_sum

print(missingInUnsorted([1,2,4], 1, 4))
print(missingInUnsorted([1,2,3,4,6], 1, 6))

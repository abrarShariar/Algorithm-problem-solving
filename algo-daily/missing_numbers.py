# SOLVED
def missing_numbers(num_arr):
	low = num_arr[0]
	high = num_arr[len(num_arr) - 1]
	arr_index = 0
	missing = []

	for i in range(low, high + 1):
		if arr_index > len(num_arr):
			break

		if num_arr[arr_index] != i:
			print(missing)
			missing.append(i)
			continue
		
		arr_index += 1

	return missing


print(missing_numbers([1,2,4,5,7]))

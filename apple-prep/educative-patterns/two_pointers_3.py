def make_squares(arr):
	squares = [0 for x in arr]
	res_index = len(arr) - 1

	start_pointer, end_pointer = 0, len(arr) - 1
	while start_pointer < len(arr) and start_pointer < end_pointer:
		if (arr[start_pointer]) ** 2 > (arr[end_pointer]) ** 2:
			squares[res_index] = (arr[start_pointer]) ** 2
			start_pointer += 1
		else:
			squares[res_index] = (arr[end_pointer]) ** 2
			end_pointer -= 1

		res_index -= 1

	squares[0] = arr[start_pointer]
	return squares

print(make_squares( [-3, -1, 0, 1, 2]))
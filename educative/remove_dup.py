def remove_duplicates(arr):
	next_spot = 1
	current = 1
	while current < len(arr):
		# next spot is free for insertion
		if arr[current] != arr[next_spot - 1]:
			arr[next_spot] = arr[current]
			next_spot += 1

		current += 1

	# print(arr)
	return next_spot


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

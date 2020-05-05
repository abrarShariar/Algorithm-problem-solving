# solved
def remove_element(arr, key):
	spot = 0
	current = 0
	while current < len(arr):
		if arr[current] != arr[spot]:
			arr[spot], arr[current] = arr[current], arr[spot]
			spot += 1
		current += 1

	return spot


def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))


main()
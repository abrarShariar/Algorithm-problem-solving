def binary_search(arr, key):
	# determine if sorted in desc or asc
	isAsc = 1
	if arr[0] > arr[len(arr) - 1]:
		isAsc = 0
	
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = left + int(((right - left)/2))
		if arr[mid] == key:
			return mid
		
		# for asc
		if key > arr[mid]:
			if isAsc == 1:
				left = mid + 1
			else:
				right = mid - 1
		else:
			if isAsc == 1:
				right = mid - 1
			else:
				left = mid + 1

	return -1


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()

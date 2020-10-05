def quickSort(left, right, input):
	left = 0
	right = len(input) - 1
	mid = left + int(((right - left)/2))
	pivot = input[mid]

	while left < right:
		if left == mid:
			left += 1
			continue
		elif right == mid:
			right -= 1
			continue

		elif input[left] > pivot:
			if input[right] < pivot:
				input[left], input[right] = input[right], input[left]
				left += 1
				right -= 1
			else:
				right -= 1

		else:
			if input[right] < pivot:
				left += 1
			else:
				left += 1
				right -= 1
		
	
	print()
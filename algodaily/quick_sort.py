def quick_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		# set the pivot
		pivot = arr[0]
		# make the list with elements less than pivot
		less_arr = [x for x in arr[1:] if x <= pivot]
		# make the list with elements greater than pivot 
		right_arr = [x for x in arr[1:] if x > pivot]
		# return
		return quick_sort(less_arr) + [pivot] + quick_sort(right_arr)

print(quick_sort([100, 9, 8, 7, 4, 1, 2, 100]))
print(quick_sort([100]))
print(quick_sort([]))

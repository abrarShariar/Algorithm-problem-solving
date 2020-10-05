def mergeSort(arr, left_index, right_index):
	if left_index < right_index:
		mid = (left_index + (right_index - left_index)) // 2
		
		mergeSort(arr, left_index, mid)
		mergeSort(arr, mid + 1, right_index)
		merge(arr, left_index, mid, right_index)

def merge(arr, left_index, mid, right_index):
	# length of the left arr
	

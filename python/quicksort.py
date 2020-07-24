# OK!
# QUICKSORT

data = [10,2,3,4,5,1,100]

def quickSort (arr, low, high):
	if low <= high:
		# get the partion index
		pi = getPartition(arr, low, high)
		quickSort(arr, pi + 1, high)
		quickSort(arr, low, pi - 1)
	return arr

def getPartition (arr, low, high):
	i = low - 1
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1


print(quickSort(data, 0, len(data)-1))





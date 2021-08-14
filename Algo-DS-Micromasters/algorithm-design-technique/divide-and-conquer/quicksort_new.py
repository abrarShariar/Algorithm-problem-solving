def quick_sort(A, l, r):
	if l >= r:
		return
	
	# partition item
	m = partition(A, l, r)

	# sort the left and right of parition
	quick_sort(A, l, m-1)
	quick_sort(A, m+1, r)
	

def partition(A, l, r):
	# take the leftmost item as pivot, x = A[l]
	pivot_index = l
	pivot_item = A[pivot_index]
	
	# index for <= elements
	j = pivot_index
	for i in range(pivot_index + 1, r + 1):
		# we swap if the current item is less than or equal to the pivot. 
		# This way we keep all the elements less than pivot on the left and all element greater to the right
		if A[i] <= A[pivot_index]:
			# we don't increment j unless we find elements that are less than 
			j = j + 1
			A[i], A[j] = A[j], A[i]
	
	# swap and put the pivot in correct positiion
	A[pivot_index], A[j] = A[j], A[pivot_index]

	# return the new pivot index
	return j

ll = [10,9,8,7,6,5,4,3,2,1]
quick_sort(ll, 0, len(ll) - 1)
print(ll)
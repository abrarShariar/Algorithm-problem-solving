import random

def qs(item_list, left_index, right_index):
	if left_index >= right_index:
		return 

	# get the pivot
	m1, m2 = get_pivot3(item_list, left_index, right_index)

	qs(item_list, left_index, m1 - 1)
	qs(item_list, m2 + 1, right_index)

def get_pivot(item_list, left_index, right_index):
	# get a random pivot index
	random_index = get_random(left_index, right_index)
	# swap with the left item
	item_list[left_index], item_list[random_index] = item_list[random_index], item_list[left_index]
	
	pivot_index = left_index
	pivot_item = item_list[pivot_index]
	j = pivot_index

	for i in range(pivot_index + 1, right_index + 1):
		if item_list[i] <= pivot_item:
			j += 1
			item_list[j], item_list[i] = item_list[i], item_list[j]

	item_list[j], item_list[pivot_index] = item_list[pivot_index], item_list[j]
	return j

def get_pivot3(A, l, r):
	lt = l
	gt = r
	i = l
	pivot = A[l]

	while i <= gt:
		if A[i] < pivot:
			A[i], A[lt] = A[lt], A[i]
			lt += 1
			i += 1
		elif A[i] > pivot:
			A[i], A[gt] = A[gt], A[i]
			gt -= 1 
		else:
			i += 1 

	return lt, gt

def get_random(l, r):
	return random.randint(l, r)


ll = [2,3,9,2,2]
qs(ll, 0, len(ll) - 1)
print(ll)



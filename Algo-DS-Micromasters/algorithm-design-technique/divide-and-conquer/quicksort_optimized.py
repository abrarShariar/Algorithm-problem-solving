import random

def qs(item_list, left_index, right_index):
	if left_index >= right_index:
		return 

	# get the pivot
	m = get_pivot(item_list, left_index, right_index)

	qs(item_list, left_index, m - 1)
	qs(item_list, m+1, right_index)

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

def get_random(l, r):
	return random.randint(l, r)


ll = [10,9,8,7,5,3,1,100,200]
qs(ll, 0, len(ll) - 1)
print(ll)



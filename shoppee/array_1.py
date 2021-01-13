# Find the first non-repeating element in an array of integers

# with hash map
def first_non_repeating(arr):
	dict = {}

	# O(n)
	for item in arr:
		dict[item] = dict.get(item, 0) + 1
	
	# O(n)
	for item in arr:
		if dict[item] == 1:
			return item

	return None

# further optimization
def first_non_repeating_op(arr):
	dict = {x: [] for x in arr}

	# O(n)
	for i in range(len(arr)):
		dict[arr[i]].append(i)

	# loop over hash map
	for key in dict.keys():
		if len(dict[key]) == 1:
			return key

	return None

if __name__ == '__main__':
	print(first_non_repeating_op([1,3,4,5,4,5,1,10]))
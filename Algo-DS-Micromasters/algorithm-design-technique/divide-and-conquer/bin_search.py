# Uses python3
import sys

# recursive way
# def binary_search_recrusive(input_list, needle):
# 	left = 0
# 	right = len(input_list) - 1
# 	mid = (right - left) // 2

# 	# base case
# 	if len(input_list) == 0 or (len(input_list) == 1 and input_list[0] != needle):
# 		return -1

# 	if input_list[mid] == needle:
# 		return mid
# 	elif needle > input_list[mid]:
# 		return binary_search_recrusive(input_list[mid+1:], needle)
# 	elif needle < input_list[mid]:
# 		return binary_search_recrusive(input_list[:mid], needle)

# iterative way
def binary_search(input_list, needle):
	left = 0
	right = len(input_list) - 1
	while left <= right:
		mid = (right + left) // 2
		if input_list[mid] == needle:
			return mid
		elif needle > input_list[mid]:
			left = mid + 1
		elif needle < input_list[mid]:
			right = mid - 1
	
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	m = data[n + 1]
	a = data[1 : n + 1]
	
	for x in data[n + 2:]:
		# replace with the call to binary_search when implemented
		print(binary_search(a, x), end = ' ')

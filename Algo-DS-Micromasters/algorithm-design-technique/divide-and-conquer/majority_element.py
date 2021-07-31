# Uses python3
import sys

def get_majority_element(item_list, left, right):
	count_dict = {}
	majority = len(item_list) / 2

	# O(n)
	for i in item_list:
		count_dict[i] = count_dict.get(i, 0) + 1

	# O(n)
	for key, value in count_dict.items():
		if value > majority:
			return key

	return -1
   
if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)

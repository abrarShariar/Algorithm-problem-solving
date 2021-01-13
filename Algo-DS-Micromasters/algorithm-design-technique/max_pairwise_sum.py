def max_pairwise(num_list):
	num_list.sort()
	return num_list[len(num_list) - 1] * num_list[len(num_list) - 2]

n = int(input())
input_list = list(map(int, input().split(' ')))
print(max_pairwise(input_list))
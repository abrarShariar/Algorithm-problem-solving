def main():
	# take input
	line = input().split(" ")
	M = int(line[0])
	X = int(line[1])
	# dictionary for each class
	dict = {}
	apple_list_sort = []
	seq = []
	total = 0
	for i in range(M):
		num_apple = int(input())
		# for maintaining insertion order
		apple_list_sort.append(num_apple)
		# [number of apple, remaining]
		dict[num_apple] = [num_apple, num_apple]
		seq.append(num_apple)
		total += num_apple

	# sort 
	apple_list_sort.sort(reverse = True)
	# output 
	target = 0
	for i in range(len(apple_list_sort)):
		apple_class = apple_list_sort[i]
		rem = X - target
		if rem >= dict[i][1]:
			dict[apple_class][1] = 0
		else:
			dict[apple_class][1] -= rem

		target += dict[apple_class][0]
		if target == X:
			break
	
	# print success
	if target == X:
		print("Thanks", X)
		for key in dict.keys():
			print(dict[key][0], dict[key][0] - dict[key][1],dict[key][1])


main()
def find_max(input_string):
	running_counter = 0
	max_counter = 0

	for i in range(len(input_string)):
		current_ch = input_string[i]
		if current_ch == '#':
			max_counter = max(max_counter, running_counter)
			running_counter = 0
		else:
			running_counter += 1

	return max(max_counter, running_counter)

print(find_max('#__###_____#_#__###______##'))
print(find_max('#####'))
print(find_max('#__###_____#_#__###__________'))

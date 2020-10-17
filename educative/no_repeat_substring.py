def get_long_sub(input_str):
	global_max_len = 0
	local_len = 0
	sub_dict = {}

	# O(n)
	for i in range(len(input_str)):
		ch = input_str[i]
		if ch in sub_dict.keys():
			# start the count again
			global_max_len = max(global_max_len, local_len)
			sub_dict[ch] = i
			local_len = 1
		else:
			sub_dict[ch] = i
			local_len += 1
	
	return global_max_len

input_str = input()
mx_str = get_long_sub(input_str)
print(mx_str)
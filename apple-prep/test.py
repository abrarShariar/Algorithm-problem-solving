def unique_char_count(input_str):
	char_dict = {}
	unique_char_count = 0
	
	# O (n)
	for char in input_str:
		char_dict[char] = char_dict.get(char, 0) + 1
		if char_dict[char] == 1:
			unique_char_count += 1
		elif char_dict[char] > 1:
			unique_char_count -= 1

	# O(n)
	# for key, value in char_dict.items():
	# 	print(key, " => ", value)
	# 	if value == 1:
	# 		unique_char_count += 1
	
	print("Number of unique char: ", unique_char_count)

input_str = input()
unique_char_count(input_str)	



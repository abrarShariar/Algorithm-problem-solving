def caesarCipherEncryptor(string, key):
	lower_limit = ord('a')
	upper_limit = ord('z')
	result_list = []

	for ch in string:
		new_pos = ord(ch) + key
		while new_pos > upper_limit:
			new_pos = new_pos - upper_limit
			new_pos = (lower_limit + new_pos) - 1

		result_list.append(chr(new_pos))

	return "".join(result_list)

# print(caesarCipherEncryptor("xyz", key = 2))
	

def get_ascii(char):
	ascii_num = ord(char)
	return ascii_num


# my_str = input("Input string: ")
# for char in my_str:
# 	print("char = ", get_ascii(char))

# change chars in strings
name = "Abrar Shariar"
name[0] = "X"

# this will throw an error because strings are immutable
print(name)


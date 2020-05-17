import itertools

def compress(input_str):
	key_func = lambda x: x[0]

	for key, group in itertools.groupby(input_str, key_func):
		el_count = len(list(group))
		print("("+str(el_count)+", "+str(key)+")", end=" ")

input_line = input()
compress(input_line)

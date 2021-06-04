# SOLVED
def sort_string(input_string):
	return " ".join(sorted(input_string.split(' '), key = lambda x: x[0].lower()))

print(sort_string("banana ORANGE apple"))
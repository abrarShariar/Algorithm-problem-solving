import random

target_str = 'methinks it is like a weasel'
all_letters = 'abcdefghijklmnopqrstuvwxyz'
all_char = [x for x in all_letters] + [' ']

def main():
	count = 0
	is_matched = False
	temp = ['0' for x in target_str]
	g_str = "".join(temp)

	while not is_matched:
		count += 1
		g_str = generate_string(g_str)

		if is_perfect_match(g_str) == True:
			print("Found string after ", count)
			print(g_str)
			exit()
		else:
			print(g_str, count)

def is_perfect_match(g_str):
	global target_str

	for i in range(len(target_str)):
		if target_str[i] != g_str[i]:
			return False

	return True
	

def generate_string(g_str):
	global target_str, all_char

	current_list = [ch for ch in g_str]

	for i in range(len(current_list)):
		if current_list[i] != target_str[i]:
			n = random.randint(0, len(all_char) - 1)
			replace_char = all_char[n]
			
			current_list[i] = replace_char

	return "".join(current_list)
		
main()
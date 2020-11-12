import random

target_str = 'methinks it is like a weasel'
all_letters = 'abcdefghijklmnopqrst'
all_char = [x for x in all_letters] + [' ']

def main():
	count = 0
	is_matched = False
	temp = ['-1' for x in target_str]
	g_str = "".join(temp)

	while not is_matched:
		count += 1
		g_str = generate_string(g_str)

		if g_str == target_str:
			print(g_str)
			print("Found string after ", count)

		elif not count%1000:
			print(g_str, count)

def generate_string(g_str):
	global target_str, all_char

	current_list = [ch for ch in g_str]

	for i in range(len(current_list)):
		if current_list[i] == '-1':
			n = random.raundint(0, len(all_char) - 1)
			replace_char = all_char[n]
			
			current_list[i] = replace_char
	
	return "".join(current_list)

def matched_pattern (result_list):
	global target_str

	for i in range(len(result_list)):
		if result_list[i] not in target_str:
			result_list[i] = '-1'

	return result_list

main()
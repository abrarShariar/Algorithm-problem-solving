def merge_the_tools(string, k):
	n = len(string)
	if n == 1 or k == 1:
		for ch in string:
			print(ch)
		return

	split_times = int(n / k)
	for i in range(0, split_times):
		num_dict = {}
		for j in range(k*i, k*i + k):
			num_dict[string[j]] = 1

		print("".join([str(s) for s in num_dict.keys()]))

if __name__ == '__main__':
  string, k = input(), int(input())
  merge_the_tools(string, k)
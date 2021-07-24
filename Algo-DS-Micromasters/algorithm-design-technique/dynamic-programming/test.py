#Uses python3

import sys

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	
	n = data[0]
	data = data[1:]
	a = data[:n]

	data = data[n:]
	m = data[0]
	data = data[1:]
	b = data[:m]

	print(data)
	print(a)
	print(b)
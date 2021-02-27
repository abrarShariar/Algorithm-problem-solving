#Uses python3
import sys

def max_dot_product(a, b):
	#write your code here
	a.sort()
	b.sort()
	
	max_product_sum = 0
	
	for i in range(len(a)):
		max_product_sum = max_product_sum + (a[i] * b[i])
	
	return max_product_sum
	
	
	
if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	a = data[1:(n + 1)]
	b = data[(n + 1):]
	print(max_dot_product(a, b))
	

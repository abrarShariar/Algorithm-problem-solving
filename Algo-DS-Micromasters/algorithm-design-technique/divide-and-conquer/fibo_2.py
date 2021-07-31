# Uses python3
import sys

def fibonacci_sum_naive(n):
	fibo_store = [0, 1]
	if n <= 1:
		return fibo_store[n]

	sum = fibo_store[0] + fibo_store[1]
	for i in range(2, n+1):
		# only store the last digit
		fibo_n = (fibo_store[i-1] + fibo_store[i-2]) % 10
		fibo_store.append(fibo_n)
		sum = (sum + fibo_n) % 10

	return sum 

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	print(fibonacci_sum_naive(n))

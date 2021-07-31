# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
	fibo_store = [0, 1]
	if n <= 1:
		return fibo_store[n]

	for i in range(2, n+1):
		fibo_n_last_digit = (fibo_store[i-1] + fibo_store[i-2]) % 10
		fibo_store.append(fibo_n_last_digit)

	return fibo_store[n]

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	print(get_fibonacci_last_digit_naive(n))

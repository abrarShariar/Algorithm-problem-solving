# Uses python3
import sys

def fibonacci_sum_naive(n):
	fibo_store = [0, 1]
	last_digit_sum_run = 1


	# if we mod by 60, the last digit starts repeating
	# https://www.py4u.net/discuss/204192
	mod_num = n % 60
	# now find the last digit sum of mood_num, n = mod_num
	n = mod_num
	
	if n == 0 or n == 1:
		return fibo_store[n]

	for i in range(2, n+1):
		fibo_n = (fibo_store[i-1] + fibo_store[i-2]) % 10
		fibo_store.append(fibo_n)
		last_digit_sum_run = (last_digit_sum_run + fibo_n) % 10

	return last_digit_sum_run

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	print(fibonacci_sum_naive(n))
		
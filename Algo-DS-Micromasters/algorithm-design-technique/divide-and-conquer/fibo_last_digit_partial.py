# SOLVED
# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):

	from_ = from_ % 60
	to = to % 60

	from_sum = 0
	to_sum = 0

	# calculate all fibo till to
	fibo_store = [0, 1]
	for i in range(2, to + 1):
		fibo_n = fibo_store[i-1] + fibo_store[i-2]
		fibo_store.append(fibo_n)

	# calculate sum from from to t
	running_sum = 0
	for i in range(from_, to + 1):
		running_sum += fibo_store[i]

	return running_sum % 10

if __name__ == '__main__':
	input = sys.stdin.read();
	from_, to = map(int, input.split())
	print(fibonacci_partial_sum_naive(from_, to))
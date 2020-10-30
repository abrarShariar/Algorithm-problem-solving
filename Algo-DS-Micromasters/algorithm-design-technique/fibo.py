# fibonacci with memoization

def fibo(n, dict):
	if n <= 1:
		return n

	key = dict.get(n, -1)

	# if the key is found
	if key == -1:
		dict[n] = fibo(n-1, dict) + fibo(n-2, dict)
	# if the key is already exists
	return dict[n]

n = int(input()) 
print(fibo(n, {}))


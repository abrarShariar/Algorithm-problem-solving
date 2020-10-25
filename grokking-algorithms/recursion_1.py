def countdown(n):
	if n <= 0:
		return
	print(n)
	countdown(n-1)

countdown(10)
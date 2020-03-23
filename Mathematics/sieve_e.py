import math

n = 100
list_num = [x for x in range(2, n+1)]
#primes = []

for i in range(0, math.ceil(math.sqrt(n)+1)):
	if list_num[i] != -1:
		start = list_num[i]
		#primes.append(start)
		if i != 0:
			jump = 2*start
		else:
			jump = start
		j = i+jump
		while j < len(list_num):
			list_num[j] = -1
			j += jump


for i in range(0, len(list_num)):
	if list_num[i] != -1:
		print(list_num[i])

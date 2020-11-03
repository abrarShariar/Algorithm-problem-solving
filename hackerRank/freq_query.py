#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuerxy function below.
def freqQuery(queries):
	freq_dict = {}
	freq_freq_dict = {}
	result = []

	for i in range(len(queries)):
		index = queries[i][0]
		key = queries[i][1]

		if index == 1:
			prev_freq = freq_dict.get(key, 0)
			freq_dict[key] = prev_freq + 1
			
			if prev_freq > 0:
				freq_freq_dict[prev_freq] = freq_freq_dict.get(prev_freq, 0) - 1

			freq_freq_dict[prev_freq + 1] = freq_freq_dict.get(prev_freq + 1, 0) + 1
		
		elif index == 2:
			if freq_dict.get(key, 0) > 0:
				freq_freq_dict[freq_dict[key]] -= 1 
				freq_dict[key] -= 1
				freq_freq_dict[freq_dict[key]] = freq_freq_dict.get(freq_dict[key], 0) + 1

		elif index == 3:
			if freq_freq_dict.get(key, 0) > 0:
				result.append(1)
			else:
				result.append(0)

	return result

if __name__ == '__main__':
		# fptr = open(os.environ['OUTPUT_PATH'], 'w')

		q = int(input().strip())

		queries = []

		for _ in range(q):
				queries.append(list(map(int, input().rstrip().split())))

		ans = freqQuery(queries)

		print(ans)
		# fptr.write('\n'.join(map(str, ans)))
		# fptr.write('\n')

		# fptr.close()

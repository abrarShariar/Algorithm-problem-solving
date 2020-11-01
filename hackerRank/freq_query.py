#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
	num_dict = {}
	freq_dict = {}
	result_list = []

	for i in range(0, len(queries)):
		index_var = queries[i][0]
		key_var = queries[i][1]

		if index_var == 1:
			prev_freq = num_dict.get(key_var, 0)
			num_dict[key_var] = prev_freq + 1
			
			if prev_freq != 0:
				freq_dict[prev_freq] -= 1
			
			freq_dict[num_dict[key_var]] = freq_dict.get(num_dict[key_var], 0) + 1
		
		elif index_var == 2:
			if num_dict.get(key_var, 0) > 0:
				prev_freq = num_dict.get(key_var, 0)
				num_dict[key_var] = prev_freq - 1

				if prev_freq != 0:
					freq_dict[prev_freq] += 1

				freq_dict[num_dict[key_var]] = freq_dict.get(num_dict[key_var], 0) - 1

		elif index_var == 3:
			if freq_dict.get(key_var, 0) <= 0:
				result_list.append(0)
			else:
				result_list.append(1)

	return result_list

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

		fptr.close()

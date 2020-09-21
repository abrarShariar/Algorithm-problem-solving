#!/bin/python3

# TIME LIMIT EXCEED :(

import math
import os
import random
import re
import sys

def freqQuery(queries):
	result_dict = {}
	output_list = []

	# O(n)
	for item in queries:
		index = item[0]
		xyz = item[1]
		
		if index == 1:
			# O(1)
			result_dict[xyz] = result_dict.get(xyz, 0) + 1
		elif index == 2:
			# O(1)
			if result_dict.get(xyz, 0) != 0:
				result_dict[xyz] = result_dict[xyz] - 1
		elif index == 3:
			isFound = False
			# O(n*m)
			if xyz in result_dict.values():
				output_list.append(1)
			else:
				output_list.append(0)

	return output_list



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
    print('\n')

    # fptr.close()

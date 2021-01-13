#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
	dict = {}
	count = 0

	for ch in s1:
		dict[ch] = dict.get(ch, 0) + 1
	
	for ch in s2:
		if dict.get(ch, 0) > 0:
			count += 1
			dict[ch] = dict[ch] - 1

	return count

if __name__ == '__main__':
		# fptr = open(os.environ['OUTPUT_PATH'], 'w')

		s1 = input()

		s2 = input()

		result = commonChild(s1, s2)

		print(result)
		# fptr.write(str(result) + '\n')

		# fptr.close()

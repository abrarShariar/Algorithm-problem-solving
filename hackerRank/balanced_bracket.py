#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
	b_stack = []
	is_valid = 0
	for ch in s:
		if ch == '{' or ch == '[' or ch == '(':
			b_stack.append(ch)
		else:
			if len(b_stack) == 0:
				return "NO"
			top_item = b_stack.pop()
			if not ((ch == ')' and top_item == '(') or (ch == '}' and top_item == '{') or ( ch == ']' and top_item == '[')): 
					return "NO"

	if len(b_stack) == 0:
		return 'YES'
	else:
		return 'NO'

if __name__ == '__main__':
		# fptr = open(os.environ['OUTPUT_PATH'], 'w')

		t = int(input())

		for t_itr in range(t):
				s = input()

				result = isBalanced(s)

				# fptr.write(result + '\n')

				print(result)

		# fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
	moves = 0
	i = len(q) - 1
	while i >= 0:
		o_i = i + 1
		if (q[i] - o_i > 2):
			print("Too chaotic")
			return
		if q[i] == o_i - 1:
			q[i], q[o_i - 2] = q[o_i - 2], q[i]
			moves += 1
		elif q[i] == o_i - 2:
			q[]
			moves += 2
		if q[i] == o_i:
			i -= 1

	print(moves)

#minimumBribes([2,1,5,3,4])
#minimumBribes([2,5,1,3,4])
minimumBribes([1,2,5,3,7,8,6,4])

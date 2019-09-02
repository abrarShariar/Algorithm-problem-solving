#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
	moves = 0
	for i in range (0, len(q)):
		if (q[i] - (i+1) > 2):
			print("Too chaotic")
			return
		for j in range (max(0, q[i] - 2), i):
			if q[j] > q[i]:
				moves += 1

	print(moves)


minimumBribes([2,1,5,3,4])
minimumBribes([2,5,1,3,4])

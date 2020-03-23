#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
	total_bribes = 0
	for i in range(0, len(q)):
		o_index = i + 1
		if (q[i] > o_index):
			if (q[i] - o_index > 2):
				print("Too chaotic")
				return
			total_bribes += (q[i] - o_index)	

	print(total_bribes)
	

minimumBribes([2,1,5,3,4])
minimumBribes([2,5,1,3,4])
minimumBribes([1,2,5,3,7,8,6,4])

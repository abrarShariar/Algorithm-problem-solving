#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
	keyboards.sort(reverse=True)
	drives.sort(reverse=True)
	i, j = 0, 0

	while i < len(keyboards) and j < len(drives):
		if (keyboards[i] + drives[j] <= b):
			return keyboards[i] + drives[j]

		if keyboards[i] >= b or drives[j] >= b:
			return -1

		if keyboards[i] >= drives[j] and keyboards[i] < b:
			j += 1
		elif keyboards[i] <= drives[j] and drives[j] < b:
			i += 1
		 
print(getMoneySpent([3,1], [5,2,8], 10))

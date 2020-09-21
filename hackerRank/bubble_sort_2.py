#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
	isSorted = False
	numSwaps = 0

	while not isSorted:
		isSorted = True
		for i in range(0, len(a) - 1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
				numSwaps += 1
				isSorted = False
	
	print("Array is sorted in " + str(numSwaps) + " swaps.")
	print("First Element: " + str(a[0]))
	print("Last Element: " + str(a[len(a) - 1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

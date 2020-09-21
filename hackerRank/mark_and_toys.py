#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
	# sort prices
	prices.sort()
	running_sum = 0
	counter = 0

	for i in range(len(prices)):
		running_sum += prices[i]
		counter += 1
		if running_sum > k:
			running_sum -= prices[i]
			counter -= 1
	
	return counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(str(result) + '\n')

    # fptr.close()

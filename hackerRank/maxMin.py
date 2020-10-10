#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
	arr = sorted(arr)
	start_pointer = 0
	end_pointer = k - 1
	min_diff = arr[end_pointer] - arr[start_pointer]
	while end_pointer < len(arr):
		min_diff = min(arr[end_pointer] - arr[start_pointer], min_diff)
		start_pointer += 1
		end_pointer += 1

	return min_diff
		


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
	d_count = 0
	for i in range(len(s) - 1):
		if s[i] == s[i+1]:
			d_count += 1
	
	return d_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result) + '\n')

    # fptr.close()

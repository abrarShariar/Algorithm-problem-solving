#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    is_valid = True
    bribes = 0
    for index in range(1, len(q) + 1):
        node = int(q[index - 1])
        diff = 0
        if node > index:
            diff = node - index
            bribes += diff
            if diff > 2:
                is_valid = False
                break
        print("index: {0}, diff: {1} ".format(index, diff))

    if is_valid:
        print(bribes)
    else:
        print("Too chaotic")

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

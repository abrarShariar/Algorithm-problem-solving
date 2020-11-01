#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
  q = int(input())
  result_dict = {}
  result_list = []
  for i in range(0, q):
    line = list(map(int, input().split(' '))
    index_x = line[0]
    value = line[1]
    if index_x == 1:
      result_dict[value] = result_dict.get(value, 0) + 1
    elif index_x == 2:
      if result_dict.get(value, -1) != -1:
        result_dict[value] -= 1
    elif index_x == 3:
      if value in result_dict.values():
        result_list.append(1)
      else:
        result_list.append(0)
  
  return result_list
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

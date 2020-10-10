#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
  order_dict = {}
  for i in range(len(orders)):
    order = orders[i]
    order_dict[i + 1] = order[0] + order[1]
  
  # sort by value
  order_dict = {k: order_dict[k] for k in sorted(order_dict, key=order_dict.get)}
  
  result = []
  for key in order_dict.keys():
    result.append(key)
  
  return result


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

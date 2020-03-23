#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(balls):
    total = 0
    for i in range(0, len(balls)):
        total = total + ((0.5) * balls[i])

    return total


balls = [1,2,2,2]
print(solve(balls))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     balls_count = int(input())
#     balls = []
#
#     for _ in range(balls_count):
#         balls_item = int(input())
#         balls.append(balls_item)
#
#     result = solve(balls)
#     fptr.write(str(result) + '\n')
#     fptr.close()

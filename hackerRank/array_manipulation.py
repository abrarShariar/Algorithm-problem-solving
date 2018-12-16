#!/bin/python3

def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    # take input for queries and update
    for i in range(queries):
        start, end, val = input().strip().split(' ')
        start, end, val = [int(start), int(end), int(val)]
        for j in range(start-1, end):
            arr[j] += val

    # find the max
    return max(arr)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
result = arrayManipulation(n, m)
print(result)

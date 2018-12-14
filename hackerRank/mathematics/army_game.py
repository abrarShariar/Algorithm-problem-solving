#!/bin/python3
# SOLVED: https://www.hackerrank.com/challenges/game-with-cells/problem

def gameWithCells(n, m):
    return int((((n%2)+n)*((m%2)+m))/4)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
result = gameWithCells(n, m)
print(result)

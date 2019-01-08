# SOLVED: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-at-the-graph-factory/
n = int(input())
edges = list(map(int, input().split()))
sum = 0
for x in edges:
    sum += x

e = sum/2

if n == e + 1:
    print("Yes")
else:
    print("No")

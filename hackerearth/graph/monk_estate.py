# SOLVED: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-in-the-real-estate/
t = int(input())
for i in range(t):
    A = set()
    roads = int(input())
    for r in range(roads):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        A.add(x)
        A.add(y)
    print(len(A))

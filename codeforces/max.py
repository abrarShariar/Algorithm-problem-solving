# SOLVED: https://codeforces.com/contest/1141/problem/B
n = int(input())
line = list(input().strip().split(' '))
current_rest = 0
max_rest = 0
round = 0

while round < 2:
    for i in range(n):
        if line[i] == '1':
            current_rest += 1
        elif line[i] == '0':
            current_rest = 0

        max_rest = max(current_rest, max_rest)

    round += 1

print(max_rest)

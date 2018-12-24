# !/bin/python3
N, M = input().strip().split(" ")
N, M = [int(N), int(M)]

arr = [0 for i in range(N+1)]

for i in range(M):
    p, q, sum = input().strip().split(" ")
    p, q, sum = [int(p), int(q), int(sum)]
    arr[p] += sum
    if q + 1 <= N:
        arr[q+1] -= sum


# print(arr)
# find max
x = 0
max = 0
for i in range(1, N+1):
    x += arr[i]
    if x > max:
        max = x

print(max)




































#
# def arrayManipulation(n, queries):
#     arr = [0]*(n+1)
#     # take input for queries and update
#     for i in range(queries):
#         start, end, val = input().strip().split(' ')
#         start, end, val = [int(start), int(end), int(val)]
#         for j in range(start-1, end):
#             arr[j] += val
#
#     # find the max
#     return max(arr)
#
# n, m = input().strip().split(' ')
# n, m = [int(n), int(m)]
# result = arrayManipulation(n, m)
# print(result)

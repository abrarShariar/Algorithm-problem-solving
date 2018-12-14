# RUNTIME ERROR
N, M = input().strip().split(' ')
N, M = [int(N), int(M)]

arr = []

for i in range(N):
    temp = []
    rows = input().strip().split(' ')
    rows = list(map(lambda x: int(x), rows))
    arr.append(rows)

k = int(input())

# get values based on k and sort
new_list = {}
for i in range(N):
    new_list[arr[i][k]] = i

# sort dict based on values
sorted_list = sorted(new_list.keys())

# output the shit out
for i in range(N):
    for j in range(M):
        print(arr[new_list[sorted_list[i]]][j], end=" ")
    print("")

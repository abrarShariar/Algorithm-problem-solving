# PARTIAL
n, m, k = input().strip().split(' ')
n, m, k = [int(n), int(m), int(k)]

node_values = list(map(int, input().split(' ')))
d = {}
for i in range(n+1):
    d[i] = []

for i in range(m):
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]
    d[x].append(y)
    d[y].append(x)

for key, value in d.items():
    if key != 0:
        if k <= len(value):
            new_list = sorted(value, key=lambda x: (node_values[x-1], -x), reverse=True)
            print(new_list[k-1])
        else:
            print(-1)









# node_values = [2,4,3]
# d = {
#     1: [2,3],
#     2: [1,3],
#     3: [1,2]
# }
#
#
# for key, value in d.items():
#     print(value)
#     # sort value based on node_values[x]
#     new_list = sorted(value, key=lambda x: node_values[x-1], reverse=True)
#     print(new_list)
#
#
#

















# # FIX CODE
# n, m, k = input().strip().split(' ')
# n, m, k = [int(n), int(m), int(k)]
#
# values = list(map(int, input().split(' ')))
#
# adjacency_list = [[] for x in range(n)]
# for i in range(m):
#     x,y = input().strip().split(' ')
#     x,y = [int(x), int(y)]
#     adjacency_list[x-1].append(y-1)
#     adjacency_list[y-1].append(x-1)
#
# value_list = [[] for x in range(n)]
# for i in range(len(adjacency_list)):
#     value_list[i] = list(map(lambda x: values[x], adjacency_list[i]))
#     value_list[i].sort(reverse=True)
#     adjacency_list[i].sort(reverse=True)
#
# # output
# for i in range(len(value_list)):
#     item = value_list[i][k-1]
#     for j in range(len(adjacency_list[i])):
#         if values[adjacency_list[i][j]] == item:
#             print(adjacency_list[i][j] + 1)

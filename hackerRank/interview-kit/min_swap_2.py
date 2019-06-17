# n = int(input())
# origin = [1, 2, 3, 4, 5]
# n = 5
# items = [2, 1, 5, 3, 4]

T = int(input())
for x in range(T):
    n = int(input())
    items = list(input().strip().split(' '))
    print(items)
    graph = {}
    for i in range(len(items)):
        graph[int(items[i])] = i + 1

    is_visited = [False for x in items]
    sum = 0
    edge_count = 0

    for i in range(len(items)):
        key = i + 1
        node = graph[key]
        if is_visited[node-1] == True:
            sum += edge_count
            edge_count = 0
        else:
            edge_count += 1
            is_visited[i] = True


    print(sum)


# print(is_visited)
# print(sum)

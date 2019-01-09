
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

keys = input().strip().split(' ')
color_list = list(map(int, keys))

occur = dict(zip(keys, [0] * len(keys)))

for x in keys:
    occur[x] += 1

occur = dict([(k, occur[k]) for k in sorted(occur, key=occur.get, reverse=True)])

color = 1
for key, value in occur.items():
    if value > k:
        print("NO")
        exit(0)
    else:
        for i in range(len(keys)):
            if keys[i] == key:
                color_list[i] = color
                color += 1
                if color > k:
                    color = 1


print("YES")
for i in range(len(color_list)):
    if i < len(color_list):
        print(color_list[i], end=" ")

import tracemalloc

tracemalloc.start()

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
multisets = [[] for i in range(n+1)]
ans = []

def gcd(a, b):
    if a == 0 :
        return b

    return gcd(b%a, a)

for i in range(q):
    in_row = input().strip().split(' ')
    in_row = list(map(int, in_row))
    if in_row[0] == 1:
        multisets[in_row[1]] = [in_row[2]]
    elif in_row[0] == 2:
        multisets[in_row[1]] = multisets[in_row[2]] + multisets[in_row[3]]
    elif in_row[0] == 3:
        # event 3
        result = []
        for i1 in multisets[in_row[2]]:
            for i2 in multisets[in_row[3]]:
                result.append(gcd(i1,i2))

        multisets[in_row[1]] = result
    elif in_row[0] == 4:
        #event 4
        ans.append((multisets[in_row[1]].count(in_row[2]))%2)

for i in ans:
    print(i, end="")
# 
# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')
#
# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)

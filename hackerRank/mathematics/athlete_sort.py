# SOLVED: https://www.hackerrank.com/challenges/python-sort-sort/problem
import operator

def sort_and_shit(N, M):
    arr = []
    for i in range(N):
        rows = input().strip().split(' ')
        rows = list(map(lambda x: int(x), rows))
        arr.append(rows)

    k = int(input())

    filter_dict = {}
    for i in range(N):
        filter_dict[i] = arr[i][k]

    sorted_dict = sorted(filter_dict.items(), key=operator.itemgetter(1))

    # print output
    for x in sorted_dict:
        for i in range(M):
            print(arr[x[0]][i], end=" ")
        print("")


N, M = input().strip().split(' ')
N, M = [int(N), int(M)]
sort_and_shit(N,M)

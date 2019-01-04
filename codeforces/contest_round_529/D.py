# SOLVED: https://codeforces.com/contest/1095/problem/D
def check (arr,a,b):
    next = -1
    l = a
    r = b
    ans = []
    for i in range(1, len(arr)):
        ans.append(l)
        if (arr[l][0] == r):
            next = arr[l][1]
        elif (arr[l][1] == r):
            next = arr[l][0]
        else:
            return 0

        l = r
        r = next

    # print result
    for i in ans:
        print(i, end=" ")

    exit()



def main ():
    n = int(input())
    arr = [[] for x in range(n+1)]
    # print(arr)
    for i in range(1,n+1):
        x, y = input().strip().split(" ")
        x, y = [int(x), int(y)]
        arr[i].append(x)
        arr[i].append(y)


    check(arr, 1, arr[1][0])
    check(arr, 1, arr[1][1])


main()

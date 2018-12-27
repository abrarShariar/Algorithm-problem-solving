# NOT SOLVED
def get_moves(arr, n, m):
    moves = 0
    # generate remainder array
    rem_arr = []
    for i in range(n):
        rem_arr.append(arr[i]%m)

    for r in range(m):
        c = n/m
        for i in range(n):
            if c <= 0:
                break
            if rem_arr[i] == r and rem_arr[i] != -1:
                c -= 1
                rem_arr[i] = -1

        if c > 0:


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
arr = input().strip().split(' ')
arr = list(map(lambda x: int(x), arr))

get_moves(arr, n, m)

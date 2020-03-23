# FIX THIS SHIT

def compare(el):
    return el[0]

def main():
    n = int(input())
    a = input().split(' ')

    l = 0
    r = n -1
    lst = 0
    seq = ""
    res = []

    while l < r:
        pair = []
        if int(lst) < int(a[l]):
            pair.append([a[l], 'L'])
        if int(lst) < int(a[r]):
            pair.append([a[r], 'R'])

        if len(pair) == 0:
            break
        elif len(pair) == 2:
            pair_sorted = sorted(pair, key=compare)
        else:
            pair_sorted = pair

        seq += pair_sorted[0][1]
        res.append(pair_sorted[0][0])
        lst = pair_sorted[0][0]

        if pair_sorted[0][1] == 'L':
            l += 1
        else:
            r -= 1

    if l == r and a[l] > res[len(res) - 1]:
        res.append(a[l])
        seq += 'L'

    print(len(res))
    print(seq)


if __name__ == '__main__':
    main()


# 10
# 1 2 5 9 10 8 7 6 4 3

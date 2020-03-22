def main():
    n = input()
    a = list(map(int, input().split(' ')))
    res = []
    seq = []

    i = 0
    j = i+1
    while i < j:
        if len(res) == 0:
            if a[i] < a[j]:
                res.append(a[i])
                i += 1
                seq.append('L')
            else:
                res.append(a[j])
                j -= 1
                seq.append('R')

        elif a[i] > res[len(res) - 1] and a[j] > res[len(res) - 1]:
            if a[i] < a[j]:
                res.append(a[i])
                i += 1
                seq.append('L')
            else:
                res.append(a[j])
                j -= 1
                seq.append('R')

        elif a[i] < res[len(res) - 1] and a[j] > res[len(res) - 1]:
            res.append(a[j])
            j -= 1
            seq.append('R')
        elif a[j] < res[len(res) - 1] and a[i] > res[len(res) - 1]:
            res.append(a[i])
            i+=1
            seq.append('L')


    if i == j and a[i] > res[len(res) - 1]:
        res.append(a[i])
        seq.append('L')


    print(res)


    return { 'len': len(res), 'seq': "".join(seq) }


if __name__ == '__main__':
    result = main()
    print(result['len'])
    print(result['seq'])

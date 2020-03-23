def main():
<<<<<<< HEAD
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
=======
    n = int(input())
    seq = list(map(int, input().split(' ')))

    i = 0
    j = len(seq) - 1
    res = []
    res_seq = []

    while i < j:
        if len(res) == 0:
            if seq[i] < seq[j]:
                res.append(seq[i])
                i += 1
                res_seq.append('L')
            else:
                res.append(seq[j])
                j -= 1
                res_seq.append('R')

        elif seq[i] == res[len(res) - 1]:
            i += 1

        elif seq[j] == res[len(res) - 1]:
            j -= 1

        elif seq[i] > res[len(res) - 1] and seq[j] > res[len(res) - 1]:
            if seq[i] < seq[j]:
                res.append(seq[i])
                i += 1
                res_seq.append('L')
            else:
                res.append(seq[j])
                j -= 1
                res_seq.append('R')

        else:
            if seq[i] > res[len(res) - 1]:
                res.append(seq[i])
                res_seq.append('L')
                i += 1
            elif seq[j] > res[len(res) - 1]:
                res.append(seq[j])
                res_seq.append('R')
                j -= 1
            else:
                break

    if i == j and len(res) == 0:
        res.append(seq[i])
        res_seq.append('L')

    elif i == j and seq[i] > res[len(res) - 1]:
        res.append(seq[i])
        res_seq.append('R')
    elif i == j and seq[i] < res[len(res) - 1]:
        res.append(seq[i])
        res_seq.append('L')

    print(len(res))
    print("".join(res_seq))


if __name__ == "__main__":
    main()
>>>>>>> b4ef197e89b9efc766e13bb7c37a5db796db7600

def main():
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

def main():
    [n, q] = list(map(int, input().strip().split(' ')))
    deq = input().strip().split(' ')
    dict = {}
    max_m = 0
    m_arr = []
    for i in range(q):
        m = int(input())
        m_arr.append(m)
        if m > max_m:
            max_m = m

    a = 0
    b = a + 1
    r = 0
    for j in range(1, max_m + 1):
        if j == m_arr[r]:
            dict[str(j)] = [deq[a], deq[b]]
            r = r+1

        if int(deq[a]) < int(deq[b]):
            deq.append(deq[a])
        else:
            deq.append(deq[b])
            deq[b] = deq[a]
        i = i+1
        del deq[0]

    if bool(dict) == False:
        return None

    for k in m_arr:
        print(dict[str(k)][0], dict[str(k)][1])

if __name__ == '__main__':
    main()

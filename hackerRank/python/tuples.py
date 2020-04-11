if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    tup = ()
    for i in range(len(integer_list)):
        el = integer_list[i]
        tup = tup + (el,)
    print(hash(tup))

# Problem link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1051
#  TIME LIMIT EXCCEEDED
# for printing to file
# import sys
# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f

import math

def main():
    while True:
        inp = int(input())
        if inp == 0:
            return
        if inp == 1:
            print('yes')
            continue

        N = inp
        arr = []
        ct = 0
        while N%2 == 0:
            ct += 1
            N = N/2

        if ct > 0:
            arr.append(ct)
            ct = 0

        for i in range(3, int(math.sqrt(N))+1,2):
            ct = 0
            while N%i == 0:
                ct += 1
                N = N/i
            if ct > 0:
                arr.append(ct)

        if N > 2:
            print('no')
            continue

        # print thy factors
        fac = 1
        for x in arr:
            fac = (x+1) * fac

        if fac%2 == 0:
            print('no')
        else:
            print('yes')


if __name__ == "__main__":
    main()
    # for printing to file
    # sys.stdout = orig_stdout
    # f.close()

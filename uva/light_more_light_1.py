# Problem link: https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1051
# TIME LIMIT EXCCED


# for printing to file
import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

import math

def main():
    while True:
        inp = int(input())
        if inp == 0:
            return
        if inp == 1:
            print('yes')
            continue

        N, count, i = inp, 2, 2
        limit = math.sqrt(N)
        while i <= limit:
            if N % i == 0:
                count += 2
            if i == limit:
                count -= 1
                break
            i += 1

        if count%2 == 0:
            print('no')
        else:
            print('yes')

if __name__ == "__main__":
    main()
    # for printing to file
    sys.stdout = orig_stdout
    f.close()

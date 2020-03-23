# problem link: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=976
# ACCEPTED

# for printing to file
# import sys
# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f

def main():
    while True:
        input_arr = input().split(" ")
        if input_arr[0] == '0' and input_arr[1] == '0':
            break

        n1 = int(input_arr[0])
        n2 = int(input_arr[1])
        ct = 0
        carry = 0

        while (n1 or n2):
            r1 = int(n1 % 10)
            r2 = int(n2 % 10)
            n1 = int(n1 / 10)
            n2 = int(n2 / 10)
            sum = r1 + r2 + carry
            if sum >= 10:
                carry = 1
                ct += 1
            else:
                carry = 0

        if (ct == 0):
            print("No carry operation.")
        elif (ct == 1):
            print(ct, "carry operation.")
        else:
            print(ct, "carry operations.")


if __name__ == "__main__":
    main()
    # for printing to file
    # sys.stdout = orig_stdout
    # f.close()

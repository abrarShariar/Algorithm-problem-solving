# problem link: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=976
# def main():
#     while True:
#         input_arr = input().split(" ")
#         if (input_arr[0] == "0" and input_arr[1] == "0"):
#             break
#         if (len(input_arr[0]) > len(input_arr[1])):
#             arr1 = input_arr[0]
#             arr2 = input_arr[1]
#         else:
#             arr1 = input_arr[1]
#             arr2 = input_arr[0]
#
#         i = len(arr1) - 1
#         j = len(arr2) - 1
#         ct = 0
#         carry = 0
#         while (i >= 0):
#             n2 = 0
#             if j >= 0:
#                 n2 = int(arr2[j])
#             n1 = int(arr1[i])
#             sum = n1 + n2 + carry
#             if sum >= 10:
#                 ct += 1
#                 carry = 1
#             i -= 1
#             j -= 1
#
#         if (ct == 0):
#             print("No carry operation.")
#         elif (ct == 1):
#             print(ct, "carry operation.")
#         else:
#             print(ct, "carry operations.")

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
            r1 = n1 % 10
            r2 = n2 % 10
            n1 = n1 / 10
            n2 = n2 / 10
            sum = r1 + r2 + carry
            if sum >= 10:
                carry = 1
                ct += 1

        if (ct == 0):
            print("No carry operation.")
        elif (ct == 1):
            print(ct, "carry operation.")
        else:
            print(ct, "carry operations.")


if __name__ == "__main__":
    main()

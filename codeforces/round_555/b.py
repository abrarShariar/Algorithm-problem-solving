def main():
    n = int(input())
    num = list(input())
    f_num = list(input().split(' '))

    start_index = 0
    for i in range(len(num)):
        if (int(num[i]) < int(f_num[int(num[i]) - 1])):
            break
        start_index += 1


    for j in range(start_index, len(num)):
        if int(num[j]) > int(f_num[int(num[j]) - 1]):
            break
        num[j] = f_num[int(num[j]) - 1]

    print("".join(num))

if __name__ == "__main__":
    main()

# 4
# 1234
# 1 1 4 5 1 1 1 1 1

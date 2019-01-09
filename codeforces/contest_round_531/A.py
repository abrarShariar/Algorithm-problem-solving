
n = int(input())
A = []
B = []
sum_A = 0
sum_B = 0

diff_list = [-1 for i in range(n+1)]
# print(diff_list)

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    A.append(1)
    B.append(n)

    sum_A += 1
    sum_B += n


    for j in range(2, n):
        # print("j= ",j)
        min_diff = n
        min_num = 0
        min_arr = ''
        for i in range(2, n):
            if diff_list[i] == -1:
                temp_diff_A = abs((sum_A+i) - (sum_B))
                temp_diff_B = abs((sum_A) - (sum_B+i))

                if temp_diff_A < temp_diff_B:
                    if temp_diff_A <= min_diff:
                        min_diff = temp_diff_A
                        min_num = i
                        min_arr = 'A'
                else:
                    if temp_diff_B <= min_diff:
                        min_diff = temp_diff_B
                        min_num = i
                        min_arr = 'B'

                # print(min_diff)

        if min_arr == 'A':
            A.append(min_num)
            sum_A += min_num
        else:
            B.append(min_num)
            sum_B += min_num

        diff_list[min_num] = 1



# print(A)
# print(B)
print(abs(sum_A - sum_B))

N, K = input().strip().split(' ')
N, K = [int(N), int(K)]
window_size = N - K + 1
vote_list = list(input().strip().split(' '))
vote_list = [int(x) for x in vote_list]

start_index = 0
end_index = start_index + (window_size - 1)

while end_index < N:
    # optimize: do in 1 loop
    # check for non-decreasing/non-incresing
    count_non_decrease = 0
    count_non_increasing = 0
    for i in range(start_index + 1, end_index + 1):
        if vote_list[i] >= vote_list[i-1]:
            count_non_decrease += 1
        # else:
        #     count_non_decrease = -1

        if vote_list[i] <= vote_list[i-1]:
            count_non_increasing += 1
        # else:
        #     count_non_increasing = -1
    # result = (0 if count_non_decrease == -1 else count_non_decrease) - (0 if count_non_increasing == -1 else count_non_increasing)
    result = (count_non_decrease + 1 if count_non_decrease > 0 else 0) - (count_non_increasing + 1 if count_non_increasing > 0 else 0)
    print(result)

    start_index += 1
    end_index += 1

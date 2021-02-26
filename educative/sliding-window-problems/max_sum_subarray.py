def max_sub_array_of_size_k(k, arr):
    running_sum = 0
    max_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        if window_end < k:
            running_sum += arr[window_end]
        else:
            max_sum = max(running_sum, max_sum)
            running_sum -= arr[window_start]
            running_sum += arr[window_end]
            window_start += 1

    max_sum = max(running_sum, max_sum)
    return max_sum


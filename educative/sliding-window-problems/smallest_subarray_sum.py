
# SOLVED
def smallest_subarray_with_given_sum(s, arr):
    window_start, running_sum, min_window_size, window_end = 0, 0, len(arr), -1

    while window_end < len(arr) and window_start < len(arr):
        if running_sum < s:
            window_end += 1
            if window_end >= len(arr):
                break
            running_sum += arr[window_end]
        else:
            min_window_size = min(min_window_size, (window_end - window_start) + 1)
            running_sum -= arr[window_start]
            window_start += 1

    return min_window_size


# SOLVED!
def longestPeak(array):
    # find the peaks
    peak_indices = []
    current_window_size = 0
    max_peak_size = current_window_size
    start_index = 1
    # O(n)
    while start_index < len(array) - 1:
        # if the current index is greater than the adjacent two indices => we found a peak
        current_peak_index = start_index
        left_slope_index = current_peak_index - 1
        right_slope_index = current_peak_index + 1

        if not (array[current_peak_index] > array[left_slope_index] and array[current_peak_index] > array[right_slope_index]):
            start_index += 1
            continue

        # move to left slope index
        while left_slope_index >= 0 and array[left_slope_index] < array[left_slope_index + 1]:
            left_slope_index -= 1

        # move to right slope index
        while right_slope_index < len(array) and array[right_slope_index] < array[right_slope_index - 1]:
            right_slope_index += 1
        
        current_window_size = (right_slope_index - left_slope_index) - 1
        max_peak_size = max(current_window_size, max_peak_size)
        start_index = right_slope_index - 1
    
    return max_peak_size

input_list = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longest_peak(input_list))



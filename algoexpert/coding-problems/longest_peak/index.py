# SOLVED!

def longest_peak(array):
    # find the peaks
    peak_indices = []
    for i in range(1, len(array) - 1):
        # if the current index is greater than the adjacent two indices
        current_peak = array[i]
        left_adjacent_el = array[i-1]
        right_adjacent_el = array[i+1]

        if current_peak > left_adjacent_el and current_peak > right_adjacent_el:
            peak_indices.append(i)

    max_peak_size = 0
    # finding the longest peak now
    for peak_index in peak_indices:
        current_peak = array[peak_index]
        left_slope_index = peak_index - 1
        right_slope_index = peak_index + 1

        # check left slope
        while left_slope_index >= 0 and array[left_slope_index] < array[left_slope_index + 1]:
            left_slope_index -= 1
        
        # check right slope
        while right_slope_index < len(array) and array[right_slope_index] < array[right_slope_index - 1]:
            right_slope_index += 1

        current_window_size = (right_slope_index - left_slope_index) - 1
        max_peak_size = max(current_window_size, max_peak_size)
    
    return max_peak_size

input_list = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longest_peak(input_list))



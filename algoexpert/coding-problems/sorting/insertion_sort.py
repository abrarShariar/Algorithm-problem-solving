def insertionSort(array):
    for i in range(1, len(array)):
        current_rolling_index = i
        while current_rolling_index > 0 and array[current_rolling_index] < array[current_rolling_index - 1]:
            array[current_rolling_index], array[current_rolling_index - 1] = array[current_rolling_index - 1], array[current_rolling_index]
            current_rolling_index -= 1
        
    return array

print(insertionSort([4,3,2,1]))
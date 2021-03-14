def selectionSort(array):
    
    for i in range(len(array) - 1):
        # find the minimun item in the i+1 window
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        # swap the min item
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

print(selectionSort([4,3,2,1]))

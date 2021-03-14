def bubbleSort(array):
    isSorted = False

    while not isSorted:
        isSorted = True
        
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
                
    return array


def binarySearch(array, target):
    # Write your code here.
    if array[0] == target:
        return 0
    start = 0
    end = len(array) 
    
    while start < end:
        mid = (end+start) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
        
    return -1

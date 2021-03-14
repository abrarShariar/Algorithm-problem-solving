def findThreeLargestNumbers(array):
    # take the first 3 items as the current largest
    current_largest_list = [array[0], array[1], array[2]]
    current_largest_list.sort()

    for i in range(3, len(array)):
        current_item = array[i]
        if current_item > current_largest_list[0]:
            current_largest_list[0] = current_item
            current_largest_list.sort()
    
    return current_largest_list

print(findThreeLargestNumbers([10,5,9,10,12]))
         
# def quickSort(array):
#     # Write your code here.
#     if len(array) <= 1:
#         return array

#     left = 0
#     right = len(array)
#     m = getPartition(array, left, right)
#     quickSort(array[left:m])
#     quickSort(array[m+1:right+1])

    

# # THIS WORKS!
# def getPartition(array, left, right):
#     if left < right:
#         pivot = array[left]
        
#         i = left + 1
#         j = left
#         while i < len(array):
#             if array[i] < pivot:
#                 j = j+1
#                 array[i], array[j] = array[j], array[i]
            
#             i += 1

#         array[left], array[j] = array[j], array[left]        
#         return j 


# input_list = [10,9,3,2,1,100]
# quickSort(input_list)
# print(input_list)


def quickSort(array):
    leftIndex = 0
    rightIndex = len(array) - 1
    return quickSortHelper(array, leftIndex, rightIndex)


def quickSortHelper(array, leftIndex, rightIndex):



def quickSortHelper(array, left_index, right_index):
    # if there is only 1 element in the array then return
    if left_index >= right_index:
        return array
    
    # make the leftmost element as pivot
    pivot = array[left_index]

    while right_index >= left_index and left_index < len(array) and right_index >= 0:
        # swap 
        if array[left_index] > pivot and array[right_index] <= pivot:
            array[left_index], array[right_index] = array[right_index], array[left_index]

        # move the left_index if left item is smaller than or equal pivot
        if array[left_index] <= pivot:
            left_index += 1
        # move the right_index if the right item greater than pivot
        if array[right_index] >= pivot:
            right_index -= 1
    
    partitionIndex = right_index
    # after this loop the value of right_index will be pointing an item which is swapable with the pivot
    array[right_index], array[0] = array[0], array[right_index]
    
    # call the quick sort helper again on the left and right partitioned array
    quickSortHelper(array[leftIndex: partitionIndex + 1], leftIndex, partitionIndex)
    quickSortHelper(array[partitionIndex+1: len(array) - 1], partitionIndex + 1, len(array) - 1)


input_list = [8,4,3,2,10,9,7]
quickSort(input_list)
print(input_list)
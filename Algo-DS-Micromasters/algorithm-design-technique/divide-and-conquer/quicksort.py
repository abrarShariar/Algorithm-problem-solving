# QUCIKSORT

# the partition steps in own words:
# 1. take the leftmost item as the pivot
# 2. create two pointers => i for the left + 1 and j = left
# 3. loop with the i index till the end
# 4. our goal is to make two separate windows
    # 1. the j index tracks the items which are less than pivot
    # 2. the i index tracks the items which are greter than pivot
# 5. so anytime we find an item in A[i] < pivot => swap with the A[j+1]...since j is the last item which is less than pivot
# 6. at last we swap the leftmost item (the pivot) with the j (since the A[j] is ofcourse less than the pivot)
# KEY NOTE: lists are mutable => passing it into functions actually modifies it 
# QUICK sort is an inplace algo


def partition(A, left, right):
    # take the pivot
    pivot = A[left]
    i = left + 1
    j = left
    while i < right:
        if A[i] <= pivot:
            j += 1
            A[i], A[j] = A[j], A[i]
        
        i+= 1
    
    # swap the pivot
    A[left], A[j] = A[j], A[left]
    # return j since j is the index where the pivot is located
    return j

# print(partition(arr, 0, len(arr)))
def quick_sort(A, left, right):
    if left < right:
        # find the partition point
        m = partition(A, left, right)
        quick_sort(A, left, m)
        quick_sort(A, m+1, right)

# quick sort is an in place sorting algorithm => the input list is updated
input_list = [6,4,2,3,9,8,9,4,7,6,1]
quick_sort(input_list, 0, len(input_list))
print(input_list)


    


# DONE

def mergeSort(input_list):
    # if we only have 1 element => return it
    if len(input_list) == 1:
        return input_list
    
    # find the mid point
    mid_point = len(input_list) // 2

    # get the left list
    left_list = input_list[0:mid_point]
    right_list = input_list[mid_point:len(input_list)]

    # sort the left list
    left_list = mergeSort(left_list)
    # sort the right list
    right_list = mergeSort(right_list)

    return merge(left_list, right_list)


def merge(left_list, right_list):
    # create the new return list
    result_list = []
    left_index, right_index = 0, 0
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            result_list.append(left_list[left_index])
            left_index += 1
        else:
            result_list.append(right_list[right_index])
            right_index += 1

    while left_index < len(left_list):
        result_list.append(left_list[left_index])
        left_index += 1
    
    while right_index < len(right_list):
        result_list.append(right_list[right_index])
        right_index += 1
    
    return result_list


    
print(mergeSort([99,98,7,3,1,2]))


def firstDuplicateValue(array):
    dup_dict = {}
    for el in array:
        if el in dup_dict:
            return el
        else:
            dup_dict[el] = 1

    return -1

print(firstDuplicateValue([2,1,5,2,3,3,4]))

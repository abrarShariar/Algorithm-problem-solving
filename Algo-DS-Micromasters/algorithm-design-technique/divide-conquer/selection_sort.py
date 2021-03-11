# selection sort

def selection_sort(input_list):
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[i]:
                # swap the two
                input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list

print(selection_sort([3,2,1,100,99]))
# def arrayOfProducts(array):
#     # Write your code here.
# 	# xor of all elements'
#     xor_el = 0
#     for i in range(len(array)):
#         xor_el = xor_el ^ array[i]

#     result_list = []
#     for i in range(len(array)):
#         result_list.append(array[i] ^ xor_el)

#     return result_list


# print(arrayOfProducts([5,0,1,4,2]))
# 

def arrayOfProducts(array):
    left_list = [1 for x in array]
    right_list = [1 for x in array]

    # populate left_list
    for i in range(len(array) - 1):
        left_list[i + 1] = array[i] * left_list[i] 
    
    # populate the right list
    for i in range(len(array) - 1, 0, -1):
        right_list[i - 1] = array[i] * right_list[i]
        
    # result_list
    result_list = []
    for i in range(len(array)):
        result_list.append(left_list[i] * right_list[i])

    return result_list

print(arrayOfProducts([5,1,4,2]))
    
    



# WRONG
# def get_max_even_sum (input_arr, k):
#     even_arr = []
#     odd_arr = []
#     # sort the arr
#     input_arr.sort(reverse = True)
    
#     # separate out the even and odd arr
#     for i in range(len(input_arr)):
#         if input_arr[i]%2 == 0:
#             even_arr.append(input_arr[i])
#         else:
#             odd_arr.append(input_arr[i])
    
#     # take the max and keep track of the remaining
#     even_index, odd_index = 0, 0
#     max_sum_list = []

#     while len(max_sum_list) < k and even_index < len(even_arr) and odd_index < len(odd_arr):
#         if even_arr[even_index] > odd_arr[odd_index]:
#             max_sum_list.append(even_arr[even_index])
#             even_index += 1
#         else:
#             max_sum_list.append(odd_arr[odd_index])
#             odd_index += 1

#     while len(max_sum_list) < k:
#         if even_index < len(even_arr):
#             max_sum_list.append(even_arr[even_index])
#             even_index += 1
#         else:
#             max_sum_list.append(odd_arr[odd_index])
#             odd_index += 1

#     max_sum = sum(max_sum_list)
#     if max_sum % 2 == 0:
#         return max_sum
    
#     reverse_index = len(max_sum_list) - 1
#     while reverse_index >= 0:
#         if max_sum_list[reverse_index] % 2 == 0:

    
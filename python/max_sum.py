# WRONG
def get_max_even_sum (input_arr, k):
    even_arr = []
    odd_arr = []
    # sort the arr
    input_arr.sort(reverse = True)
    
    # separate out the even and odd arr
    for i in range(len(input_arr)):
        if input_arr[i]%2 == 0:
            even_arr.append(input_arr[i])
        else:
            odd_arr.append(input_arr[i])
    
    # take the max and keep track of the remaining
    even_index, odd_index = 0, 0
    max_sum = 0

    print(even_arr)
    print(odd_arr)

    # Go Greedy
    while k > 0:
        if k % 2 == 1:
            max_sum += even_arr[even_index]
            even_index += 1
            k -= 1
        else:
            if even_index < len(even_arr) - 1 and odd_index < len(odd_arr) - 1:
                max_sum += max(even_arr[even_index] + even_arr[even_index + 1], odd_arr[odd_index] + odd_arr[odd_index + 1])
                even_index += 2
                odd_index += 2
            elif even_index < len(even_arr) - 1:
                max_sum += even_arr[even_index] + even_arr[even_index + 1]
                even_index += 2
            else:
                max_sum += odd_arr[odd_index] + odd_arr[odd_index + 1]
                odd_index += 2
            
            k -= 2

    return max_sum        
    

print(get_max_even_sum([4,2,6,7,8], 3))

    
    
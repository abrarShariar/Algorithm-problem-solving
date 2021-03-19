def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result_list = []
    for i in range(len(array)):
        left_pointer = i + 1
        right_pointer = len(array) - 1
        rem = abs(targetSum - array[i])
        while left_pointer < right_pointer:
            current_sum = array[left_pointer] + array[right_pointer]
            if current_sum == rem:
                result_list.append([array[i], array[left_pointer], array[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
            elif current_sum < rem:
                left_pointer += 1
            elif current_sum > rem:
                right_pointer -= 1
    
    return result_list

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
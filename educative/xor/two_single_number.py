def find_single_numbers(nums):
    running_num1 = 0
    running_num2 = 0
    for i in range(len(nums) - 1):
        running_num1 = running_num1 ^ nums[i]
        running_num2 = 


def main():
    print('Single numbers are:' +
            str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()

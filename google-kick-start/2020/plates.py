number_of_test_cases = int(input())
# take input of all the test cases
for i in range(number_of_test_cases):
    number_of_stacks, number_of_plates, required_plates = list(map(int, input().split(' ')))
    stacks = []
    for j in range(number_of_stacks):
        stack = list(map(int, input().split(' ')))
        stacks.append(stack)

    current_plate_count = 0
    while current_plate_count < number_of_stacks:
        # loop over each of the stack and pop the max element

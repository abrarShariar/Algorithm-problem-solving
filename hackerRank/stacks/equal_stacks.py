n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]

cylinders = [[] for i in range(3)]
for i in range(3):
    row = list(map(int, input().split(' ')))
    cylinders[i] = row

stack_sum = {
    '0': sum(cylinders[0]),
    '1': sum(cylinders[1]),
    '2': sum(cylinders[2])
}

min_stack = sorted(stack_sum.items(), key=lambda x: x[1])
min_index = min_stack[0][0]

max_stack = sorted(stack_sum.items(), key=lambda x: x[1], reverse = True)
max_index = max_stack[0][0]

while not (sum(cylinders[0]) == sum(cylinders[1]) == sum(cylinders[2])):

    while stack_sum[max_index] > stack_sum[min_index]:
        cylinders[int(max_index)].pop(0)
        stack_sum[max_index] = sum(cylinders[int(max_index)])

    min_stack = sorted(stack_sum.items(), key=lambda x: x[1])
    min_index = min_stack[0][0]

    max_stack = sorted(stack_sum.items(), key=lambda x: x[1], reverse = True)
    max_index = max_stack[0][0]


print(stack_sum['0'])

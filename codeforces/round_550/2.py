n = int(input())
dict = {
    'even': [],
    'odd': []
}

line = input().split(' ')
num_list = [int(x) for x in line]
total_sum = sum(num_list)
x_list = []
# input
for i in range(n):
    if num_list[i] % 2 == 0:
        dict['even'].append(i)
    else:
        dict['odd'].append(i)

# output
# for starting with even
i = dict['even'].pop()
while len(num_list) > 0 and i >= 0 and i < len(num_list):
    el = num_list[i]
    x_list.append(el)

    if el % 2 == 0:
        if len(dict['odd']) <= 0:
            break
        i = dict['odd'].pop()
    else:
        if len(dict['even']) <= 0:
            break
        i = dict['even'].pop()

result = total_sum - sum(x_list)

x_list = []
if (result > 0)
    # for starting with even
    for i in range(n):
        if num_list[i] % 2 == 0:
            dict['even'].append(i)
        else:
            dict['odd'].append(i)
    i = dict['odd'].pop()
    while len(num_list) > 0 and i >= 0 and i < len(num_list):
        el = num_list[i]
        x_list.append(el)

        if el % 2 == 0:
            if len(dict['odd']) <= 0:
                break
            i = dict['odd'].pop()
        else:
            if len(dict['even']) <= 0:
                break
            i = dict['even'].pop()

    result = min(result, total_sum - sum(x_list))

print(result)

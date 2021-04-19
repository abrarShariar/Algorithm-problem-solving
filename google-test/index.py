# Write your code here
def get_min():
    num_count = int(input())
    num_list = list(map(int, input().split(' ')))
    min_num = num_list[0]

    for i in range(1, len(num_list)):
        min_num = min(num_list[i], min_num)
    
    return min_num

print(get_min())


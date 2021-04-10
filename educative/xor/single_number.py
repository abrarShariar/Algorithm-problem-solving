def find_single_number(arr):
    current_num = 0
    for i in range(len(arr)):
        current_num = current_num ^ arr[i]
    return current_num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()
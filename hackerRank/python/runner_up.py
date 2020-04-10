if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_first = -100
    max_second = -100
    for i in range(len(arr)):
        if arr[i] > max_first:
            max_second = max_first
            max_first = arr[i]
        elif arr[i] < max_first and arr[i] > max_second:
            max_second = arr[i]
    print(max_second)

# SOLVED
def fibonacci(n):
    i = 0
    arr = []
    while i < n:
        if i == 1:
            arr.append(1)
        elif i == 0:
            arr.append(0)
        else:
            arr.append(arr[i-1] + arr[i-2])
        i += 1
    return arr

n = int(input())
cube = lambda x: x**3;
print(list(map(cube, fibonacci(n))))

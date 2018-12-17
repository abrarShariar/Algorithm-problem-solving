# WRONG ANS
n = int(input())
statements = input().strip().split(' ')
arr = list(map(lambda x: int(x), statements))
# arr.sort()
new_arr = list(set(arr))
sum = sum(new_arr[0:len(new_arr)])

if sum > n:
    print("Impossible")
else:
    print("Possible")
    hat = 1
    for x in new_arr:
        if x == 0:
            for j in range(n):
                print(hat, end=" ")
        else:
            for j in range(x):
                print(hat, end=" ")
        hat += 1

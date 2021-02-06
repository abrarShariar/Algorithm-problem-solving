# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    set_a = list(set(A))
    target_num = 0
    for i in range(len(set_a)):
        target_num = i+1
        if target_num != set_a[i]:
            return target_num

    return target_num + 1


    
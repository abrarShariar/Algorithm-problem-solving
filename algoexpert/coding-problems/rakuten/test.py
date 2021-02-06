# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    binarian_A = 0
    for i in range(len(A)):
        binarian_A += pow2(A[i])

    result_list = []
    while binarian_A > 0:
        # find the closest pow
        start_index_pow2 = 0
        closest_pow2 = pow2(start_index_pow2)
        while closest_pow2 <= binarian_A:
            start_index_pow2 += 1
            closest_pow2 = pow2(start_index_pow2)
        
        result_list.append(start_index_pow2 - 1)
        binarian_A = binarian_A - pow2(start_index_pow2 - 1)

    return len(result_list)

# function to get the 2^k
def pow2(k):
    result = 1
    for i in range(k):
        result = result * 2
    
    return int(result)


print(solution([1,0,2,0,0,2]))
print(solution([1]))
print(solution([0]))
print(solution([0]))



# solution([2])
# solution([0])
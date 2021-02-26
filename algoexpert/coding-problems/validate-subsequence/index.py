# SOLVED

def isValidSubsequence(array, sequence):
    p1, p2 = 0, 0
    
    while p1 < len(array) and p2 < len(sequence):
        if array[p1] == sequence[p2]:
            p2 += 1
        p1 += 1
    
    if p2 >= len(sequence):
        return True
    return False

print(isValidSubsequence([1,2,3], [3]))
print(isValidSubsequence([1,2], [3]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))


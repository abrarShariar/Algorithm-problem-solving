# SOLVED: 
N = int(input())

row = input().strip().split(' ')
row = list(map(lambda x: int(x), row))

# check if all are positive
if(all(map(lambda x: x > 0, row))):
    # check palindromic
    isPalindromic = False
    for i in range(N):
        num_str = str(abs(row[i]))
        reverse_str = num_str[::-1]
        if num_str == reverse_str:
            print("True")
            isPalindromic = True
            break
    if(isPalindromic == False):
        print("False")
else:
    print("False")

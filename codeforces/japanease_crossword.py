# input
n,x = map(int,raw_input().split())
calc_length = n + x
a = raw_input().split()

# calculation
str = 'YES'
for index in range(0,n):
    if calc_length > int(a[index]) + 1:
        calc_length = calc_length - (int(a[index]) + 1)
    else:
        str = 'NO'
        break
    
print(str)
        



# input
n,m = map(int,raw_input().split())
array = [0 for _ in range(n+1)]

# calculation
for index in range(0,m):
    a,b,k = map(int,raw_input().split())
    for i in range(a,b+1):
        array[i] = array[i] + k
    
# output 
print max(array)

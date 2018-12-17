# PASSED
v = int(input())
n = v
i = n - 1
while i > 0:
    x = i
    if n == 1:
        break
    if n%x != 0:
        n = n-x
    i -= 1

print(n)

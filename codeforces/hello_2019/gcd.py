def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)


a = [2, 2, 3]
b = [1, 4, 6]

for i1 in a:
    for i2 in b:
        print(gcd(i1,i2))

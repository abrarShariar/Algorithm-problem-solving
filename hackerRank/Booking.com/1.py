a, b, c = input().strip().split(' ')
a, b, c = [int(a), int(b), int(c)]

if a > 0 and b > 0 and c > 0:
    isValidTriangle = False
    if (a + b > c) and (b + c > a) and (a + c > b):
        isValidTriangle = True

    if isValidTriangle:
        #check equilateral
        if len(set({a, b, c})) == 1:
            print(1)
        else:
            print(2)
    else:
        print(0)
else:
    print(0)

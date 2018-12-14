#SOLVED: https://www.hackerrank.com/challenges/lowest-triangle/problem
#!/bin/python3
def lowestTriangle(base, area):
    a = area
    height = (2 * a) / base
    if 'e-' not in str(height).split('.')[0]:
        if str(height).split('.')[1] == '0':
            return int(height)

    while a >= area:
        a = 0.5 * height * base
        h = int(height) + 1
        if h >= height:
            break
    return int(h)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)

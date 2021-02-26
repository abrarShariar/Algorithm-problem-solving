#Uses python3
# IN PROGRESS
import sys

def largest_number(a):
    #write your code here
    current_max = a[0]
    for i in range(1, len(a)):
        current_num = a[i]
        current_max = getMax(current_num, current_max)
    
    return current_max

def getMax(current_num, current_max):
    p1 = int(str(current_num) + str(current_max))
    p2 = int(str(current_max) + str(current_num))
    return max(p1, p2)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

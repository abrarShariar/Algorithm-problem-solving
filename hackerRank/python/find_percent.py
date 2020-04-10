from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    students = {}
    for i in range(n):
        line = input().split()
        students[line[0]] = Decimal(sum([float(x) for x in line[1:]])/3)

    query_name = input()
    print(round(students[query_name],2))

import math
if __name__ == '__main__':
    students = []
    min_first = float(100)
    min_second = float(100)
    for i in range(int(input())):
        name = input()
        score = float(input())
        if score < float(min_first):
            min_second = float(min_first)
            min_first = float(score)

        elif score < float(min_second) and score > float(min_first):
            min_second = float(score)

        students.append([name, score])

    nameArr = []
    for j in range(len(students)):
        if students[j][1] == min_second:
            nameArr.append(students[j][0])

    nameArr.sort()
    for name in nameArr:
        print(name)

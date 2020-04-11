N = int(input())
resultList = []
for i in range(N):
    line = input().split()
    if line[0] == 'insert':
        index = int(line[1])
        num = int(line[2])
        resultList.insert(index, num)
    elif line[0] == 'print':
        print(resultList)
    elif line[0] == 'remove':
        resultList.remove(int(line[1]))
    elif line[0] == 'append':
        resultList.append(int(line[1]))
    elif line[0] == 'sort':
        resultList.sort()
    elif line[0] == 'pop':
        resultList.pop()
    elif line[0] == 'reverse':
        resultList.reverse()

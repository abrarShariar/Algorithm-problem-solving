# RUNTIME ERROR
max_count = 0
initial = 0

class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False
        self.neighbours = []
        self.value = 0

    def addNeighour(self, n):
        self.neighbours.append(n)

def DFS(s):
    global initial
    global max_count
    # print(s.index, " ", s.value, " ", initial)
    s.visited = True
    initial += s.value

    if initial > max_count:
        max_count = initial

    for x in s.neighbours:
        if x.visited == False:
            DFS(x)

    return


def DFS_Boot(nodeList):
    global initial
    for node in nodeList:
        if node.visited == False:
            initial = 0
            DFS(node)
            # print("\n")
    return


T = int(input())
for i in range(T):
    max_count = 0
    N, M = input().strip().split(' ')
    N, M = [int(N), int(M)]
    nodeList = [Node(i) for i in range(N)]

    for i in range(M):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        nodeList[x-1].addNeighour(nodeList[y-1])
        nodeList[y-1].addNeighour(nodeList[x-1])

    bannaRow = input().strip().split(' ')
    bannaRow = list(map(lambda x: int(x), bannaRow))

    for i in range(N):
        nodeList[i].value = bannaRow[i]

    DFS_Boot(nodeList)
    print(max_count)

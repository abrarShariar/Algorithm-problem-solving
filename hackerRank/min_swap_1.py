# problem statement
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# SOLVED

# def minimumSwaps(arr):
#     if len(arr) == 1:
#         return 0
#     index = 1
#     hashMap = {}
#     swapCount = 0
#     isVisited = [False] * (len(arr)+1)
#     # print(isVisited)
#     flagSwitch = 0
#     while index <= len(arr):
#         hashMap[index] = arr[index-1]
#         index += 1
#
#     # print(hashMap.get(4))
#     position = 1
#     while flagSwitch < len(isVisited) and position <= len(arr):
#         element = hashMap.get(position)
#         # print(element)
#         if position == element:
#             isVisited[position] = True
#             flagSwitch += 1
#             position += 1
#             continue
#
#         # position = element
#         # print(position)
#         if (not(isVisited[element])):
#             swapCount += 1
#             isVisited[int(hashMap.get(position))] = True
#             flagSwitch += 1
#             position = element
#         else:
#             position = hashMap.get(position) + 1
#
#     return swapCount-1

# def minimumSwaps(arr):
#     if len(arr) == 1:
#         return 0
#
#     swapCount = 0
#     loopCount = 0
#     position = 1
#     n = len(arr)
#
#     # map position to element
#     posMap = {}
#     for i in range(1, n+1):
#         posMap[i] = arr[i-1]
#
#     # create isVisited list
#     isVisited = [False] * (n+1)
#
#     # loop over and find cycle
#     # while loopCount < n and position <= n:
#     for position in range(1, n+1):
#         element = posMap.get(position)
#         if element == position or isVisited[position]:
#             isVisited[position] = True
#             continue
#
#         if not(isVisited[position]):
#             swapCount += 1
#             isVisited[position] = True
#             # position = posMap.get(position)
#
#     # print(swapCount)
#
#     if swapCount == 0:
#         return swapCount
#     else:
#         return swapCount-1

def minimumSwaps(arr):
    if len(arr) == 1:
        return 0

    swapCount = 0
    position = 1
    n = len(arr)

    # map position to element
    posMap = {}
    for i in range(1, n+1):
        posMap[i] = arr[i-1]

    # create isVisited list
    isVisited = [False] * (n+1)

    # loop over and find cycle
    for pos in range(1, n+1):
        # if a node is already visited there is no point in computing anything -> just skip
        if (not(isVisited[pos])):
            isVisited[pos] = True
            if pos == posMap.get(pos):
                continue
            else:
                c = posMap.get(pos)
                while (not(isVisited[c])):
                    isVisited[c] = True
                    swapCount += 1
                    c = posMap.get(c)

    return swapCount


print(minimumSwaps([1,4,3,2]))
print(minimumSwaps([2,4,3,1]))
print(minimumSwaps([1,3,5,2,4,6,7]))
print(minimumSwaps([2,3,4,1,5]))
print(minimumSwaps([1]))
print(minimumSwaps([7,1,3,2,4,5,6]))
print(minimumSwaps([4, 1, 3,2]))

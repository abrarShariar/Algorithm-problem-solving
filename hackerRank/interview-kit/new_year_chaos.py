def miminimumBribes(q):
    bribes = 0
    for index in range(1, len(q) + 1):
        node = int(q[index - 1])
        if node > index:
            diff = node - index
            bribes += diff
            if diff > 2:
                is_valid = False
                break

    if is_valid:
        print(bribes)
    else:
        print("Too chaotic")




# T = int(input())
# is_valid = True
#
# for i in range(T):
#     is_valid = True
#     n = int(input())
#     items = list(input().strip().split(' '))
#     bribes = 0
#     for index in range(1, len(items) + 1):
#         node = int(items[index - 1])
#         if node > index:
#             diff = node - index
#             bribes += diff
#             if diff > 2:
#                 is_valid = False
#                 break
#
#     if is_valid:
#         print(bribes)
#     else:
#         print("Too chaotic")

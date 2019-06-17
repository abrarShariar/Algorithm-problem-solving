# SOLVED
from collections import defaultdict
n = int(input())
for i in range(n):
    text = input()
    dict = {}
    dict = defaultdict(lambda: 0, dict)
    is_valid = 1
    if len(text) <= 1:
        print("Yes")
        continue

    for j in range(len(text)):
        dict[text[j]] += 1
        if dict[text[j]] > 1:
            # print(dict[text[j]])
            is_valid = 0
            break

        is_found = 0
        for k in range(len(text)):
            if (ord(text[j]) == ord(text[k]) - 1 or ord(text[j]) == ord(text[k]) + 1):
                is_found = 1
                break

        if is_found == 0:
            is_valid = 0
            break

    if is_valid == 1:
        print("Yes")
    else:
        print("No")

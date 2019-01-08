# SOLVED:   https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/description/
keys = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

def get_match_count(num):
    match_count = 0
    if num == 0:
        return 6
    else:
        while num:
            rem = int(num%10)
            match_count += keys[rem]
            num = int(num/10)

        return match_count

T = int(input())
for i in range(T):
    num = input()
    # count the number of matches
    # match_count = get_match_count(num)
    match_count = 0
    for ch in num:
        match_count = match_count + keys[int(ch)]

    if int(match_count%2) == 0:
        digit = int(match_count/2)
        for j in range(digit):
            print(1, end="")
        print()
    else:
        digit = int(match_count/2)
        print(7, end="")
        for j in range(int(digit-1)):
            print(1, end="")
        print()

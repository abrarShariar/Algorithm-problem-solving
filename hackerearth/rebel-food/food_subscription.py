n = int(input())
day1_pack = 199
day7_pack = 699
day30_pack = 2499

if n == 30:
    print(day30_pack)
    exit(0)
elif n == 1:
    print(day1_pack)
    exit(0)

date_list = list(map(int, input().split(' ')))
sum = 0
i = 0
count = 0
while i < len(date_list):
    start = date_list[i]
    end = start+6
    count = 0
    j = i
    while j < len(date_list):
        if date_list[j] <= end:
            count += 1
        if date_list[j] > end:
            break
        j += 1

    temp = 0
    if count == 1:
        sum += day1_pack
        i += 1
    elif count > 1:
        temp = count * day1_pack
        sum += min(day7_pack, temp)
        i = j


print(min(sum, day30_pack))

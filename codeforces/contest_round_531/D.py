# FIXED in D_2
num_dict = {
    '0': 0,
    '1': 0,
    '2': 0
}

n = int(input())
limit = int(n/3)
st = input()
diff = [0 for i in range(3)]

for ch in st:
    num_dict[ch] += 1

for key, value in num_dict.items():
    diff[int(key)] = limit - value

st_list = list(st)

i,j = 0, 2
while i < 2 and j > 0:
    if diff[i] == 0:
        i += 1
    if diff[j] == 0:
        j -= 1


    # both positive
    if diff[i] > 0 and diff[j] > 0:

    # both negative
    # if diff[i] < 0 and diff[j] < 0:
    if diff[i] > 0 and diff[j] < 0:
        # start from front of st
        for m in range(len(st_list)):
            if st_list[m] == str(j):
                st_list[m] = str(i)
                diff[i] -= 1
                diff[j] += 1

            if diff[i] == 0 or diff[j] == 0:
                break

    if diff[i] < 0 and diff[j] > 0:
        for m in range(len(st_list)-1, -1, -1):
            if st_list[m] == str(i):
                st_list[m] = str(j)
                diff[i] += 1
                diff[j] -= 1

            if diff[i] == 0 or diff[j] == 0:
                break

for x in st_list:
    print(x, end="")

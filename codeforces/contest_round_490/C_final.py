import operator

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

str = input()
key_pair = {}

for i in range(len(str)):
    key_pair[i] = str[i]

sorted_dict = sorted(key_pair.items(), key=operator.itemgetter(1))
del sorted_dict[0:k]

sorted_dict = dict(sorted_dict)
sorted_dict = dict(sorted(key_pair.items(), key=operator.itemgetter(0)))

for key, value in sorted_dict.items():
    print(value, end="")

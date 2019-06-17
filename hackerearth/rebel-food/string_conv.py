x = input()
y = input()

x_dict = {}
y_dict = {}

for i in range(97, 123):
    x_dict[chr(i)] = 0
    y_dict[chr(i)] = 0

if x == y:
    print(0)
    exit(0)

for ch in x:
    x_dict[ch] += 1

for ch in y:
    y_dict[ch] += 1

x_dict = sorted(x_dict.items(), key=lambda x: x[1], reverse=True)
y_dict = sorted(y_dict.items(), key=lambda x: x[1], reverse=True)

if max(x_dict[0][1], y_dict[0][1]) == 1:
    print("Not possible")
    exit(0)


for i in range

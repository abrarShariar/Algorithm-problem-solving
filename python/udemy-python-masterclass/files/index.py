my_file = open("file.txt", "r")

# print(my_file.mode)
# print(my_file.read())
for line in my_file.readlines():
    if line.startswith('C'):
        print(line)
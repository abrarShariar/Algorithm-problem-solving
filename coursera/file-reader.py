# with open('read_file.txt') as file:
#     for line in file:
#         print(line.strip().upper())

# file = open('read_file.txt')
# data = file.readlines()
# for line in data:
#     print(line.strip())

file = open('read_file.txt')
data = file.readline()
print(data.strip())
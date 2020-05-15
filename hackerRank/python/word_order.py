# SOLVED
n = int(input())
dict = {}
for i in range(n):
	word = input()
	dict[word] = dict.get(word,0) + 1

print(len(dict.keys()))
for key in dict.keys():
	print(dict[key], end=" ")
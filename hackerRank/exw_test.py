target_word = input()
list_of_words = set(input().split())

# create dict for target word
target_dict = {}
for word in target_word:
	target_dict[word] = 1

result_count = 0

for word in list_of_words:
	temp_dict = {}
	for char in word:
		temp_dict[char] = 1
	
	if set(temp_dict.keys()) == set(target_dict.keys()):
		result_count += 1

print(result_count)

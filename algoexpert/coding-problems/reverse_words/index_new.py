# SOLVED
def reverseWordsInString(string):
	char_list = list(string)
	
	# reverse the whole string
	reverseUtility(char_list, 0, len(char_list) - 1)

	# reverse the individual words
	left_pointer = 0
	right_pointer = 0

	while right_pointer < len(char_list) and left_pointer < len(char_list):
		while right_pointer < len(char_list) and char_list[right_pointer] != ' ':
			right_pointer += 1

		reverseUtility(char_list, left_pointer, right_pointer - 1)
		left_pointer = right_pointer + 1
		right_pointer = right_pointer + 1

	return "".join(char_list)
		

def reverseUtility(char_list, start, end):
	while start < end:
		char_list[start], char_list[end] = char_list[end], char_list[start]
		start += 1
		end -= 1


input_string = "I am    abrar"
print(reverseWordsInString(input_string))
# NOT SOLVED
def reverseWordsInString(string):
	# reverse the whole input string
	reversed_list = reverseUtility(string)
	right_pointer = 0
	left_pointer = 0

	result = []

	while right_pointer < len(reversed_list):
		while right_pointer < len(reversed_list):
			if reversed_list[right_pointer] != ' ':
				right_pointer += 1
			elif reversed_list[right_pointer] == ' ':
				right_pointer -= 1
				break

		word = reversed_list[left_pointer: right_pointer + 1]
		word = "".join(word)
		word = reverseUtility(word)		
		result += word

		left_pointer = right_pointer + 1

	result_str = "".join(result)

	return result_str

def reverseUtility(input_entity):
	left_pointer = 0
	right_pointer = len(input_entity) - 1
	ll_word = list(input_entity)

	while left_pointer < right_pointer:
		ll_word[left_pointer], ll_word[right_pointer] = ll_word[right_pointer], ll_word[left_pointer]
		left_pointer += 1
		right_pointer -= 1

	return ll_word


print(reverseWordsInString("I am Abrar"))


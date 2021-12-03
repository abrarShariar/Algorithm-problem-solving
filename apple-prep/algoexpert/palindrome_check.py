# SOLVED!
def isPalindrome(string):
	# a single string is palindrome
	if len(string) == 1:
		return True
	
	start_pointer = 0
	end_pointer = len(string) - 1
	while start_pointer < end_pointer:
		if string[start_pointer] != string[end_pointer]:
			return False

		start_pointer += 1
		end_pointer -= 1
			
	return True


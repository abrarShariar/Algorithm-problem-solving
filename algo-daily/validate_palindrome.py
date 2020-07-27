def is_palindrome(s):
		ll = list(s)
		i, j = 0, len(ll) - 1
		while i <= j:
			front_char = ll[i].lower()
			back_char = ll[j].lower()
			if ord(front_char) >= 97 and ord(front_char) <= 122 and ord(back_char) >= 97 and ord(back_char) <= 122:
				if front_char != back_char:
					return False
				i += 1
				j -= 1
				continue
				
			if not(ord(front_char) >= 97 and ord(front_char) <= 122):
				i += 1
			if not(ord(back_char) >= 97 and ord(back_char) <= 122):
				j -= 1
			
		return True

print(is_palindrome('mother'))
print(is_palindrome('civic'))
print(is_palindrome('ciic'))
print(is_palindrome('cxciic$'))
print(is_palindrome('A Santa Lived As a Devil At NASA'))

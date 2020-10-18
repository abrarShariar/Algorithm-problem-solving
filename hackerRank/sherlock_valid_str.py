from collections import Counter

# DEBUG

def isValid(s):
	dict_ch_count = Counter(s)
	keys_count = Counter(dict_ch_count.values())

	if len(keys_count.values()) > 2:
		return "NO"

	elif len(keys_count.values()) == 2:
		if 1 in keys_count.values():
			return "YES"
		return "NO"

	return "YES"


print(isValid("aabbccddeefghi"))
print(isValid("abcdefghhgfedecba"))

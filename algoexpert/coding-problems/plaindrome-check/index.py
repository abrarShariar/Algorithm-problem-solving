# SOLVED IT
def isPalindrome(string):
    front_index = 0
    back_index = len(string) - 1

    while front_index <= back_index:
        if string[front_index] != string[back_index]:
            return False
        front_index += 1
        back_index -= 1


    return True


print(isPalindrome("abc"))
print(isPalindrome("abcdcba"))
print(isPalindrome("a"))

print(isPalindrome("abc"))
print(isPalindrome("abcdcba"))
print(isPalindrome(""))
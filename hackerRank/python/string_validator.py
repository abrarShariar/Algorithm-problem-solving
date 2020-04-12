if __name__ == '__main__':
    s = input()
    checkAlphaNum = False
    checkAlpha = False
    checkDigit = False
    checkLowChar = False
    checkUpChar = False
    for ch in s:
        if ch.isalnum():
            checkAlphaNum = True
        if ch.isalpha():
            checkAlpha = True
        if ch.isdigit():
            checkDigit = True
        if ch.islower():
            checkLowChar = True
        if ch.isupper():
            checkUpChar = True

    print(checkAlphaNum)
    print(checkAlpha)
    print(checkDigit)
    print(checkLowChar)
    print(checkUpChar)

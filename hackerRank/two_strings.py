# SOLVED: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def twoStrings(s1, s2):
    dic = {}
    # d2 = {}
    str1 = s1
    str2 = s2
    if len(s2) < len(s1):
        str1 = s1
        str2 = s2

    # prepare the dictionary
    for ch in str1:
        if ch not in dic:
            dic[ch] = 1

    # print(dic)
    for ch in str2:
        if ch in dic:
            return "YES"
    
    return "NO"



print(twoStrings("Hi", "Dictionry"))
print(twoStrings("hello", "world"))
print(twoStrings("hi", "world"))
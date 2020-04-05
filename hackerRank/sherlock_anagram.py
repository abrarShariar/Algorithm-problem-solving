# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

import math
import os
import random
import re
import sys

def isAnagram(st1, st2):
    if len(st1) != len(st2):
        return False

    dict1 = {}
    dict2 = {}

    for ch in st1:
        if ch in dict1.keys():
            dict1[ch] = dict1[ch] + 1
        else:
            dict1[ch] = 1

    for ch in st2:
        if ch in dict2.keys():
            dict2[ch] = dict2[ch] + 1
        else:
            dict2[ch] = 1

    for key in dict1:
        if key in dict2.keys():
            if dict1[key] != dict2[key]:
                return False
        else:
            return False

    return True

def generateSubstrings(str):
    result = []
    for i in range(0, len(str)):
        for j in range(i+1, len(str)+1):
            result.append(str[i:j])

    return result

def countAnagram(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if len(arr[i]) == len(arr[j]):
                if (isAnagram(arr[i], arr[j]) == True):
                    count = count + 1

    return count


def sherlockAndAnagrams(s):
    # check for duplicate before doing any computation

    for i in range(0, len(str)):
        for j in range(i+1, len(str)+1):
            


    # substringArr = generateSubstrings(s)
    # if len(substringArr) <= 1:
    #     return 0
    # return countAnagram(substringArr)

#
# print(sherlockAndAnagrams("abba"))
# print(sherlockAndAnagrams("abcd"))
# # print(sherlockAndAnagrams("kkkk"))
# print(sherlockAndAnagrams("kkkk"))
# print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel"))
print(sherlockAndAnagrams("gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde"))
print(sherlockAndAnagrams("mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw"))
print(sherlockAndAnagrams("ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges"))
print(sherlockAndAnagrams("zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw"))

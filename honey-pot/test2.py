#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
def funWithAnagrams(text):

    if len(text) == 0 or len(text) == 1:
        return text

    result_list = []
    anagram_list = []

    # create the first text items' anagram
    anagram_list.append(createAnagram(text[0]))
    result_list.append(text[0])

    for i in range(1, len(text)):
        item = text[i]
        # check if this item's anagram exists in the anagram_list
        if isAnagram(item, anagram_list) == False:
            # create the anagram of this item
            anagram_list.append(createAnagram(item))
            result_list.append(item)

    result_list.sort()
    return result_list

def createAnagram(item):
    anagram = {}
    for ch in item:
        anagram[ch] = anagram.get(ch, 0) + 1
    
    return anagram

def isAnagram(item, anagram_list):
    #  over each anagram in anagram list
        # check if the item chars match up with the anagram
    is_anagram = False
    
    # create a anagram dict for the item
    anagram_item_dict = createAnagram(item)
        
    for i in range(len(anagram_list)):
        is_anagram = True
        anagram_dict = anagram_list[i]

        # check if the anagram_dict and anagram_item_dict are sames
        for key, value in anagram_dict.items():
            if key not in anagram_item_dict or value != anagram_item_dict[key]:
                is_anagram = False
                break
        
        if is_anagram:
            break
    
    return is_anagram



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

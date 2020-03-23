#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
	len_s = len(s)
	count_a = s.count("a")
	return (count_a * (n // len(s))) + s[:n%len_s].count("a")



print(repeatedString("abcac", 10))
print(repeatedString("abc", 100000000000000000))
print(repeatedString("aba", 10))
print(repeatedString("aaa", 10))
print(repeatedString("gfcaaaecbg", 547602))


#Test-4
#gfcaaaecbg
#547602
#164280

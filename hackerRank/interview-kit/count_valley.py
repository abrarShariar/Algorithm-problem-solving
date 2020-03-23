#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	is_valley = 0
	is_mount = 0
	is_sea = 1

	valley_count = 0
	mount_count = 0

	v_stack = []
	m_stack = []

	for i in range(0, len(s)):
		if is_valley == 0 and is_mount == 0:
			is_sea = 1

		if s[i] == 'U':
			if (len(v_stack) != 0):
				v_stack.pop()
				if len(v_stack) == 0 and len(m_stack) == 0:
					if is_valley == 1:
						valley_count += 1
						is_valley = 0
					elif is_mount == 1:
						mount_count += 1
						is_mount = 0
				continue

			if is_sea == 1:
				is_mount = 1
				is_sea = 0
			m_stack.append('U')
		
		elif s[i] == 'D':
			if (len(m_stack) != 0): 			
				m_stack.pop()
				if len(v_stack) == 0 and len(m_stack) == 0:
					if is_valley == 1:
						valley_count += 1
						is_valley = 0
					elif is_mount == 1:
						mount_count += 1
						is_mount = 0
				continue
			if is_sea == 1:
				is_valley = 1
				is_sea = 0
			v_stack.append('D')


	return valley_count
		

print(countingValleys(8, "UDDDUDUU"))
print(countingValleys(8, "DDUUUUDD"))

# D = -1
# U = +1

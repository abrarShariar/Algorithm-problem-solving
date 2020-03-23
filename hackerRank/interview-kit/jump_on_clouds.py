import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	i = 0
	jump = 0
	
	while i < len(c) - 1:
		if (i+2) < len(c):
			if c[i+2] == 1:
				i = i+1
			else:
				i = i+2
		else:
			i = i+1

		jump = jump + 1

	return jump

print(jumpingOnClouds([0,0,0,0,1,0]))
print(jumpingOnClouds([0,0,1,0,0,1,0]))


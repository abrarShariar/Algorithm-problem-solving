# SOLVED
def power_of_three (num):
	if num == 1:
		return True

	rem = num % 3
	quo = int(num / 3)

	if rem != 0:
		return False
	
	return power_of_three(quo)

print(power_of_three(9))
print(power_of_three(10))
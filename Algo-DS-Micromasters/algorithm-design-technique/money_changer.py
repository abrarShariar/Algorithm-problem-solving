def money_changer(m):
	change_count = 0
	while m > 0:
		if m >= 10:
			m = m - 10
		elif m >= 5:
			m = m - 5
		else:
			m = m - 1
		change_count += 1

	return change_count

print(money_changer(2))
print(money_changer(28))
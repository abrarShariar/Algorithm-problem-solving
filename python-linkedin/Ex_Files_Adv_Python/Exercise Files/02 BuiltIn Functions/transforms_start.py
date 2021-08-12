# use transform functions like sorted, filter, map


def filterFunc(x):
	pass


def filterFunc2(x):
	pass


def squareFunc(x):
	pass


def toGrade(x):
	if x >= 94:
		return 'A+'
	elif x >= 90:
		return 'A'
	elif x >= 85:
		return 'A-'
	elif x >= 80:
		return 'B'
	elif x >= 70:
		return 'C'


def main():
	# define some sample sequences to operate on
	nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
	chars = "abcDeFGHiJklmnoP"
	grades = (81, 89, 94, 78, 61, 66, 99, 74)

	# TODO: use filter to remove items from a list
	filtered_data = list(filter(lambda x: x%2 == 0, nums))
	print(filtered_data)

	filterdAlphabets = list(filter(lambda x: x >= 'A' and x <= 'Z', chars))
	print(filterdAlphabets)
	# TODO: use filter on non-numeric sequence

	# TODO: use map to create a new sequence of values
	new_list = list(map(lambda x: x + 'zzzz', chars))
	print(new_list)

	squares = list(map(lambda x: x*x, nums))
	print(squares)

	# TODO: use sorted and map to change numbers to grades
	sorted_grades = sorted(list(grades), reverse=True)
	graded = list(map(toGrade, sorted_grades))
	print(graded)


if __name__ == "__main__":
	main()

# use iterator functions like enumerate, zip, iter, next


def main():
	# define a list of days in English and French
	days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
	daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven"]

	# TODO: use iter to create an iterator over a collection
	# my_iter = iter(days)
	# first_val = next(my_iter)
	# second_val = next(my_iter)
	# print(first_val)
	# print(second_val)

	# TODO: iterate using a function and a sentinel
	# with open("testfile.txt", "r") as file_p:
	# 	for line in iter(file_p.readline, ''):
	# 		print(line)

	d = { 
		"name": 'Abrar',
		"skills": ['Python', 'Java', 'C++']
	}

	# for index, item in enumerate(d, start=1):
	# 	print(index, item)

	# TODO: use regular interation over the days

	# TODO: using enumerate reduces code and provides a counter
	# for index, day in enumerate(days, start=0):
	# 	print(index, day)
	# d1 = {
	# 	"name": 'Abrar'
	# }

	# d2 = {
	# 	"age": 90
	# }

	# for val1, val2 in zip(d1, d2):
	# 	print(val1, d1[val1], val2, d2[val2]) 

	# TODO: use zip to combine sequences


if __name__ == "__main__":
	main()

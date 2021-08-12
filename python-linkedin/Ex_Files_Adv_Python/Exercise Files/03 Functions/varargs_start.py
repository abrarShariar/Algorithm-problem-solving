# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
	print(args)
	print(len(args))
	print(type(args))

	for arg in args:
		print(arg)
    


def main():
    # TODO: pass different arguments
    addition(['123123', '1231'], ['C++', 'Python3', 'JavaScript'])

    # TODO: pass an existing list


if __name__ == "__main__":
    main()

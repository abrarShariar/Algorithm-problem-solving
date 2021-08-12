# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
	if x % 2 == 0:
		return True
	return False

def main():
	# TODO: cycle iterator can be used to cycle over a collection
	seq1 = ["Joe", "John", "Mike"]
	cycle1 = itertools.cycle(seq1)

	print(next(cycle1))
	print(next(cycle1))
	print(next(cycle1))
	print(next(cycle1))

	# TODO: use count to create a simple counter
	count1 = itertools.count(100, 10)
	print(next(count1))
	print(next(count1))
	print(next(count1))

	for c in itertools.count(100, 10):
		print(c)
		if c >= 200:
			break

	# TODO: accumulate creates an iterator that accumulates values
	vals = [10,20,30,40,50,40,30]
			
	# TODO: use chain to connect sequences together
	l1 = [1,2,4,5]
	l2 = ['Python3', 'C++', 'JavaScript']
	print(list(itertools.chain(l1, l2)))

	# TODO: dropwhile and takewhile will return values until
	# a certain condition is met that stops them
	result = itertools.takewhile(testFunction, vals)
	print(list(result))

	
	
if __name__ == "__main__":
	main()
	
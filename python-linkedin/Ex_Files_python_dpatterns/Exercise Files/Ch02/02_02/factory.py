class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"

class Cat:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"


def get_pet(pet="dog"):

	"""The factory method"""

	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
	return pets[pet]


d = get_pet()
print(d.speak())

c = get_pet('cat')
print(c.speak())

test_dict = dict(name="Hello", skills=['Python', 'JavaScript'])
print(test_dict)
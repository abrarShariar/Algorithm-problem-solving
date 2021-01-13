class Car:
	
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def getCarName(self):
		return self.name

myCar = Car("Abrar Car", "blue")
print(myCar.getCarName())

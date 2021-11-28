class Car:
	def __init__(self, name):
		self.name = name
	
car = Car("Toyota")
car_2 = car
car_3 = car
car_4 = car

print(car.name)
print(car_2.name)
print(car_4.name)

car_2.name = "BMw"

print(car.name)
print(car_2.name)
print(car_4.name)


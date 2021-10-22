#include<iostream>
#include<string>
using namespace std;

class Car {
	private:
		string name;
		double width;
	public:
		Car(string, double);
		void setName(string);
		void setWidth(double);
		string getName();
		double getWidth();
};

Car::Car(string name, double width) {
	cout << "From Constructor " << endl;
	cout << name << endl;
	cout << width << endl;
}

void Car::setName(string name) {
	this->name = name;
}

void Car::setWidth(double width) {
	this->width = width;
}

string Car::getName() {
	return this->name;
}

double Car::getWidth () {
	return this->width;
}

int main () {
	Car myCar("BMW", 9812.13);
	// Car myCar = new Car("BMW", 123.123);
	myCar.setName("Toyota");
	myCar.setWidth(99.999);
	cout << "The name of the car is: " << myCar.getName() << endl;
	cout << "The width of the car is: " << myCar.getWidth() << endl;
	// printf("The name of the car is: %s \n", myCar.getName().c_str());
	// printf("The width of the car is: %f \n", myCar.getWidth());
}
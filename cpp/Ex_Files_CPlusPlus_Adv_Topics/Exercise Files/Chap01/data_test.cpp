#include<iostream>
#include<string>
using namespace std;

struct Car {
	string name;
	double weight;
};

int main () {
	Car carArr[10];

	for (int i = 0; i < 10; i++) {
		Car car;
		car.name = "Test_" + to_string(i);
		carArr[i] = car;
	}

	// output
	for (int i = 0; i < 10; i++) {
		cout << carArr[i].name << endl;
	}
	

	// Car c1;
	// c1.name = "BMW";
	// c1.weight = 999.11;

	// cout << c1.name << endl;
}
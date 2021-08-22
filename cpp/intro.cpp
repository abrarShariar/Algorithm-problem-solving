#include<iostream>
using namespace std;

int main () {
	// int a = 10;
	// double b = 5.0;
	// printf("%f \n", a / b);

	int number_of_pennies = 7;
	switch (number_of_pennies) {
		case 10:
			cout << "Yo 10" << endl;
		case 9: 
			cout << "Yo 9" <<endl;
		case 8:
			cout << "Yo 8" <<endl;
			break;
		default:
			cout << "Default" << endl;
	}
}
#include <stdio.h>

struct Car {
	char *type;
	int number;
};

struct Car *allocateStruct();
void modify_struct(struct Car *car);
void display_struct(struct Car *car);

int main () {
	struct Car *car = allocateStruct();

	display_struct(car);
}


struct Car *allocateStruct () {
	struct Car *car;
	car = (struct Car*)malloc(sizeof(struct Car));
	return car;
}



void display_struct (struct Car *car) {
	printf("Type of the car: %s", car->type);
}
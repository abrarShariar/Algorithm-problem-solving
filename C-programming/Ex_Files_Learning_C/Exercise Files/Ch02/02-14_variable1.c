#include <stdio.h>

int main()
{
	int age;
	age = 30;

	char x, y, z;

	// x = 'C',
	// y = '+',
	// z = '+';

	// printf("%c%c%c",x,y,z);

	// // printf("The C language is over %d years old!\n",age);

	// printf("Calculate: %d + %d = %d",2,2,2+2);

	printf("Enter a Letter: ");
	char inputChar = getchar();
	printf("You have entered: %c", inputChar);
	
	return(0);
}


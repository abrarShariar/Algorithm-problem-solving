#include <stdio.h>

int main()
{
	int input_num;
	printf("Enter number: ");
	scanf("%d", &input_num);

	input_num % 2 == 0 ? printf("Even") : printf("Odd");

	// int age;
	// char *classification;

	// printf("Enter your age: ");
	// scanf("%d",&age);

	// classification = ( ( age < 19 ) ? "kid" :
	// 	( age < 65 ? "adult" :
	// 	  "geezer" ));
	// printf("You are a %s.\n",classification);

	// return(0);
}


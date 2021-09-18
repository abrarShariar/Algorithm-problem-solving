#include <stdio.h>

int main()
{
	// char name[10];
	// scanf("%s", name);
	// printf("My Skills: %s", name);


	char text[100];
	fgets(text, 100, stdin);
	printf("The text you entered: %s\n", text);

	// double dd;
	// // int x;
	// printf("Enter a double num: ");
	// scanf("%lf", &dd);
	// printf("Entered: %lf", dd);

	// printf("Type an integer: ");
	// scanf("%ld",&x);
	// printf("Integer %ld\n",x);

	return(0);
}


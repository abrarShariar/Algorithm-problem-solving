#include <stdio.h>

int main()
{


	int input_num;
	printf("Input a number: ");
	scanf("%d", &input_num);

	switch (input_num)
	{
	case 1:
		printf("RED");
		break;
	case 2:
		printf("GREEN");
		break;
	case 3:
		printf("BLUE");
		break;
	default:
		printf("INVALID OPTION");
		break;
	}

	// char input_char;
	// printf("Choose an option (A, B, C): ");
	// scanf("%c", &input_char);

	// switch (input_char)
	// {
	// case 'A':
	// 	puts("A for Apple");
	// 	break;
	// case :
	// case 'B':
	// 	puts("B for BMW");
	// 	break;
	// case 'C':
	// 	puts("C for Covalent");
	// 	break;
	// default:
	// 	puts("Invalid option");
	// 	break;
	// }


	// char a;

	// printf("Your choice (A,B,C): ");
	// scanf("%c",&a);

	// switch(a)
	// {
	// 	case 'A':
	// 		puts("Excellent choice!");
	// 		break;
	// 	case 'B':
	// 		puts("This is the most common choice.");
	// 		break;
	// 	case 'C':
	// 		puts("I question your decision.");
	// 		break;
	// 	default:
	// 		puts("That's not a valid choice.");
	// }

	// return(0);
}


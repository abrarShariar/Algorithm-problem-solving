#include <stdio.h>

int main()
{
	int c;

	// printf("Type a letter: ");
	// c = getchar();
	// printf("You typed '%c'.\n",c);
	printf("Enter your first Name char: ");
	char firstNameChar = getchar();

	printf("Enter last name char: ");
	char lastNameChar = getchar();

	printf("First: %c Last %c", firstNameChar, lastNameChar);

	return(0);
}


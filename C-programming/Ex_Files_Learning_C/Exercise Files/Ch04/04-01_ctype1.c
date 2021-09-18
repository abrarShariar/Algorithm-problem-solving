#include <stdio.h>
#include <ctype.h>

int main()
{
	char input_char;
	do {
		input_char = getchar();
		putchar(toupper(input_char));
	} while (input_char != 'X');

	// int ch = 'a';

	// printf("Original %c\n",ch);
	// printf("Lowercase %c\n",tolower(ch));
	// printf("Uppercase %c\n",toupper(ch));
	// printf("Original %c\n",ch);

	return(0);
}


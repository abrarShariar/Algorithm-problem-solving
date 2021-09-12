#include <stdio.h>
#include <ctype.h>

int main()
{
	int ch = 'a';

	printf("Original %c\n",ch);
	printf("Lowercase %c\n",tolower(ch));
	printf("Uppercase %c\n",toupper(ch));
	printf("Original %c\n",ch);

	return(0);
}


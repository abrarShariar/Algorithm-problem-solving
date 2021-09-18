#include <stdio.h>

int main()
{
	int a,b;

	printf("Type two letters: ");
	a = getchar();
	b = getchar();
	printf("You typed '");
	putchar(a);
	printf("' and '");
	putchar(b);
	printf("'.\n");

	return(0);
}


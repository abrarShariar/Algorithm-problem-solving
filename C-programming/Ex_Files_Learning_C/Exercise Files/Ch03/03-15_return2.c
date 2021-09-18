#include <stdio.h>

char gimmeAnA(void);

int main()
{
	printf("On this test you received an %c.\n",gimmeAnA());

	return(0);
}

char gimmeAnA(void)
{
	return('A');
}


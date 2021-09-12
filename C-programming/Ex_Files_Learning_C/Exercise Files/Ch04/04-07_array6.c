#include <stdio.h>

int main()
{
	char hello[] = "Greetings, human!\n";
	int n;

	n = 0;
	while( hello[n] != '\0')
	{
		putchar(hello[n]);
		n++;
	}

	return(0);
}

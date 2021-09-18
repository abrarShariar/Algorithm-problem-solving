#include <stdio.h>

int main()
{
	char *presidents[5] = {
		"Washington",
		"Adams",
		"Jefferson",
		"Madison",
		"Monroe"
	};
	int x;
	char *ptr;

	for(x=0;x<5;x++)
	{
		ptr = presidents[x];
		while(*ptr != '\0')
		{
			putchar(*ptr);
			ptr++;
		}
		putchar('\n');
	}

	return(0);
}


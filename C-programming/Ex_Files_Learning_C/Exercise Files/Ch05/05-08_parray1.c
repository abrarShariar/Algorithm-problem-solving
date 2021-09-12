#include <stdio.h>

int main()
{
	char *months[12] = {
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December"
	};
	int x;

	for(x=0;x<12;x++)
		printf("%s\n",months[x]);

	return(0);
}


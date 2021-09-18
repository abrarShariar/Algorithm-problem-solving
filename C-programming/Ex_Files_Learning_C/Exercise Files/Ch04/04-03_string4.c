#include <stdio.h>
#include <string.h>

int main()
{
	char first[] = "I would like to go ";
	char second[] = "from here to there\n";
	char buffer[50];

	strcpy(buffer,first);
	strcat(buffer,second);
	puts(buffer);

	return(0);
}


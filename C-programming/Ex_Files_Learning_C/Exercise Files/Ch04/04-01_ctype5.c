#include <stdio.h>
#include <ctype.h>

int main()
{
	int acter;

	do
	{
		acter = getchar();
		if(isdigit(acter))
			putchar(acter);
	}
	while( acter != '\n');

	return(0);
}

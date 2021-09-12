#include <stdio.h>

int main()
{
	char alpha;
	int numeric;

    alpha = 'A';
    while(alpha<'K')
	{
	    numeric = 0;
		while(numeric<10)
        {
			printf("%c-%d\t",alpha,numeric);
			numeric++;
        }
		putchar('\n');
		alpha++;
	}

	return(0);
}


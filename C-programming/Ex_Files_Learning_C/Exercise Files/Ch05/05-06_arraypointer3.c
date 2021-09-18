#include <stdio.h>

int main()
{
	int array[] = { 11, 13, 17, 19 };
	int *aptr;

	aptr = array;		/* no & needed for an array */

	printf("The element is %d\n",*aptr);

	return(0);
}


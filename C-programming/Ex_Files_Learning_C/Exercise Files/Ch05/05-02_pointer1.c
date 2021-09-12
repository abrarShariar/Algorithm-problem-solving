#include <stdio.h>

int main()
{
	int pokey;
	int *p;

	p = &pokey;
	printf("The address of `pokey` is %p\n",&pokey);
	printf("The address of `p` is %p\n",p);

	return(0);
}


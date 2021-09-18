#include <stdio.h>

int main()
{
	int pokey;
	int *p;

	pokey = 987;
	p = &pokey;

	printf("The address of `pokey` is %p\n",&pokey);
	printf("The address of `p` is %p\n",p);

	printf("The value of `pokey` is %d\n",pokey);
	printf("The value of `*p` is %d\n",*p);

	return(0);
}


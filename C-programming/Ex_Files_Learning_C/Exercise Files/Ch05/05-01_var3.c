#include <stdio.h>

int main()
{
	char a;
	short b;
	int c;
	long d;
	float e;
	double f;

	printf("A char variable occupies %lu bytes of storage\n",sizeof(a));
	printf("A short variable occupies %lu bytes of storage\n",sizeof(b));
	printf("An int variable occupies %lu bytes of storage\n",sizeof(c));
	printf("A long variable occupies %lu bytes of storage\n",sizeof(d));
	printf("A float variable occupies %lu bytes of storage\n",sizeof(e));
	printf("A double variable occupies %lu bytes of storage\n",sizeof(f));

	return(0);
}


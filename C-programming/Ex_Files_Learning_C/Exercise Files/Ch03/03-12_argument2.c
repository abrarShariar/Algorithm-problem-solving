#include <stdio.h>

void repeat(int count);

int main()
{
    int a,b;

    a = 1;
    b = 5;

	puts("At first the raven was like:");
	repeat(a);
	puts("But then he was all:");
	repeat(b);

	return(0);
}

void repeat(int count)
{
	int x;

	for(x=0;x<count;x++)
		puts("Nevermore!");
}


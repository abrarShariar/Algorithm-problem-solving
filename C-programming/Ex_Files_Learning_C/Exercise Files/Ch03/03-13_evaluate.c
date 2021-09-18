#include <stdio.h>

void evaluate(int x);
int main()
{
	int i;

	printf("Type an integer value: ");
	scanf("%d",&i);
	evaluate(i);

	return(0);
}

void evaluate(int x)
{
	if (x == 10) {
		printf("Equal to 10");
	} else if (x < 10) {
		printf("Less than 10");
	} else {
		printf("Greater than 10");
	}
}


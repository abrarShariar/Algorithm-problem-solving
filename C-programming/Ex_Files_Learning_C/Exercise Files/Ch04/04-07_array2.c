#include <stdio.h>

int main()
{
	float temps[4] = { 74.9, 73.7, 75.8, 78.2 };
	int x;

	printf("Local temperatures:\n");
	for(x=0;x<4;x++)
		printf("Station %d: %.1f\n",x,temps[x]);

	return(0);
}


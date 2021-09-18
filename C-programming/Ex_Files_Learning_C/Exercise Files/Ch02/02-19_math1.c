#include <stdio.h>
#include <math.h>

int main()
{
	float a, b;
	printf("Enter a: ");
	scanf("%f", &a);
	printf("Enter b: ");
	scanf("%f", &b);

	printf("Add %f", a + b);
	if (a > b) {
		printf("Sub %f", a - b);
	} else {
		printf("Sub %f", b - a);
	}

	printf("Pow: %f", pow(a, b));
	printf("Sqrt a: %f", sqrt(a));
	printf("Sqrt b: %f", sqrt(b));

	return(0);
}


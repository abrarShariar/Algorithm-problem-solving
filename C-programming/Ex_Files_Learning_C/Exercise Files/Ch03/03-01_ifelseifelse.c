#include <stdio.h>

int main()
{
	int a;

	printf("Type an integer: ");
	scanf("%d",&a);
	if( a > 10 )
    {
        printf("You typed %d.\n",a);
		printf("%d is greater than 10.\n",a);
    }
	else if( a < 10)
	{
        printf("You typed %d.\n",a);
		printf("%d is less than 10.\n",a);
	}
	else
	{
        printf("You typed %d.\n",a);
		printf("%d is 10.\n",a);
	}

	return(0);
}


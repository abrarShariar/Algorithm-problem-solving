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
	if(a <= 10 )
	{
        printf("You typed %d.\n",a);
        printf("%d is less than or equal to 10.\n",a);
	}

	return(0);
}


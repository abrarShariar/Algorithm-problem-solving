#include <stdio.h>

int main()
{
    int a,b;
    int *ptr;

    a = 1234;
    ptr = &a;
    b = *ptr;

    printf("A is %d and B is %d\n",a,b);

    return(0);
}

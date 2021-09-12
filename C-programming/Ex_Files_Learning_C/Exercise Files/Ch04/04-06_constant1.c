#include <stdio.h>

int main()
{
    const int x = 5;

    printf("%d squared is %d\n",x,x*x);
    x = 10;
    printf("%d squared is %d\n",x,x*x);


    return(0);
}

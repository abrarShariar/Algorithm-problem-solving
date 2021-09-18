#include <stdio.h>

int main()
{
    char a,b,c,*p;

    a = 'A';        /* assign 'A' to variable a */
    p = &a;         /* set pointer p to the address of a */
    b = *p;         /* assign variable b to the value addressed by pointer p */
    p = &c;         /* set pointer p to the address of c */
    *p = 'Z';       /* assign the value addressed by pointer p to 'Z' */

    printf("%c %c %c\n",a,b,c);

    return(0);
}

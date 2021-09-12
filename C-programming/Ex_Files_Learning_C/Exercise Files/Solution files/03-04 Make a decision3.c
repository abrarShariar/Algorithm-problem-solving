#include <stdio.h>

int main()
{
    int input;

    printf("Type a value (1,2,3): ");
    scanf("%d",&input);

    if(input==1)
        printf("Red\n");
    else if(input==2)
        printf("Green\n");
    else if(input==3)
        printf("Blue\n");
    else
        printf("Invalid input\n");

    return(0);
}

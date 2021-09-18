#include <stdio.h>

int max(int x, int y);
void isLarger(int big);

int main()
{
	int a,b,larger;

	printf("Type two integers separated by a space: ");
	scanf("%d %d",&a,&b);
	larger = max(a,b);
	if(a == larger)
		isLarger(a);
	else
		isLarger(b);

	return(0);
}
	
int max(int x, int y)
{
	if( x > y)
		return(x);
	return(y);
}

void isLarger(int big)
{
	printf("Value %d is larger.\n",big);
}


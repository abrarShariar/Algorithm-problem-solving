#include <stdio.h>

int main()
{
	char a, b, c;
	char *pchar;

	a = 'A';
	pchar = &a;

	b = *pchar;

	pchar = &c;
	
	*pchar = 'Z';

	// A, A, Z
	printf("%c %c %c", a, b, c);



	// char name[10] = "Abrar";
	// char *p_name = name;

	// *p_name = "My New";
	
	// printf("name string: %c \n", *p_name);
	// printf("name address: %p \n", &name);
	// printf("name address: %p \n", p_name);

	// int pokey;
	// int *p;

	// p = &pokey;
	// printf("The address of `pokey` is %p\n",&pokey);
	// printf("The address of `p` is %p\n",p);

	// return(0);
}


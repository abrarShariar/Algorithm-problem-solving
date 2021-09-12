#include <stdio.h>

int main()
{

	for (int i = 0; i < 10; i++) {
		printf("%d ", i);
	}

	int start = -10;
	while (start <= 10) {
		if (start % 2 == 0) {
			printf("%d ", start);
		}
		start++;
	}

	// char x;
	// printf("Start char: ");
	// scanf("%c", &x);
	
	// do {
	// 	printf("%c", x);
	// 	x++;
	// } while (x <= 'Z');

	// // int x;

	// // x = 0;
	// // while( x <= 20 )
	// // {
	// // 	if (x % 2 == 0) {
	// // 		printf("%d\n",x);
	// // 	}
	// // 	x++;
	// // }

	return(0);
}


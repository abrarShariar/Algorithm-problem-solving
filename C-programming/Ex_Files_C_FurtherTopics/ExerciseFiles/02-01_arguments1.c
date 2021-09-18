#include <stdio.h>

int main(int argc, char *argv[])
{
	printf("There were %d command line arguments\n",argc);

	// for (int i = 0; i < argc; i++) {
	// 	puts(argv[i]);
	// }

	if (argc < 2) {
		puts("Not enough arguments");
	}

	return(0);
}


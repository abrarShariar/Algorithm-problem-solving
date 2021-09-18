#include <stdio.h>
#include <string.h>
#include <ctype.h>

void modify_str(char *input_str) {
	int len = strlen(input_str);
	for (int i=0; i < len; i++) {
		input_str[i] = input_str[i] == ' ' ? '_' : toupper(input_str[i]);
	}
}

int main () {
	char input_str[256];
	printf("Input string: ");
	fgets(input_str, 256, stdin);

	modify_str(input_str);
	puts(input_str);
}
#include <stdio.h>
#include <ctype.h>
#include <string.h>

char *sort_str (char *input_str) {
	printf("%lu\n", strlen(input_str));
	printf("%ld\n", sizeof(input_str));
	printf("%ld\n", sizeof(char));
	int str_length = sizeof(input_str) / sizeof(char);
	printf("%d\n",str_length);
	// do a selection sort
	for (int i = 0; i < str_length; i++) {
		// find the min in the unsorted part
		char min_char = input_str[i];
		int min_char_index = i;
		for (int j = i + 1; j < str_length; j++) {
			if (toascii(input_str[j]) <= toascii(min_char)) {
				min_char = input_str[j];
				min_char_index = j;
			}
		}
		// swap 
		char temp = input_str[i];
		input_str[i] = min_char;
		input_str[min_char_index] = temp;
	}

	return input_str;
}

int main () {
	char input_str[100];
	printf("Enter a string: ");
	fgets(input_str, 100, stdin);
	char *result_str = sort_str(input_str);
	puts(result_str);
}


#include <stdio.h>
#include <string.h>

int main()
{
	char name[255];
	char skills[255];

	printf("Name: ");
	fgets(name, 255, stdin);
	printf("Skills: ");
	fgets(skills, 255, stdin);

	printf("Your name: %s \n", name);
	printf("Your skills: %s \n", skills);

	char full_text[255];

	strcpy(full_text, name);
	strcat(full_text, skills);

	printf("Full Text: %s", full_text);

	// char input_str[10];
	// fgets(input_str, 10, stdin);
	// int len = strlen(input_str);

	// printf("You have entered string of size: %d \n", len);
	// printf("Entered String: %s\n", input_str);
	// char string[] = "Just how long am I?";
	// int len;

	// len = strlen(string);
	// printf("The following string:\n");
	// puts(string);
	// printf("is %d characters long.\n",len);

	return(0);
}


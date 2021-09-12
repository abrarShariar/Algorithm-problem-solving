#include <stdio.h>

int main()
{
	char names[5][9] = {
		"Ant",
		"Bee",
		"Cat",
		"Duck",
		"Elephant"
	};
	int x;

	for(x=0;x<5;x++)
		printf("%s\n",names[x]);

	return(0);
}


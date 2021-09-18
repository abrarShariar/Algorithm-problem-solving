#include<stdio.h>

struct Node {
	int weight;
	char edges[10];
};

int main() {
	struct Node n1;
	n1.weight = 10;
	n1.edges = {'A'};

	return 0;
}
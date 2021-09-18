#include<stdio.h>

int *return_primes () {
	int arr[] = {2,3,5,7,11};
	return arr;
}

int main() {
	int *my_arr = return_primes();
	printf("%d", *(my_arr+1));
}
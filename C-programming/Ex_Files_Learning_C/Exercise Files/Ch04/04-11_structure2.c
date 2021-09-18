#include <stdio.h>

int main()
{
	struct bank {
		int account;
		float balance;
	};
	struct bank checking;

	checking.account = 1234;
	checking.balance = 567.89;

	printf("Checking account %d has a balance of %f\n",
        checking.account,
        checking.balance
        );

	return(0);
}


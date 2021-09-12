#include <stdio.h>

int main()
{
	struct bank {
		int account;
		float balance;
	};
	struct bank checking,savings;

	checking.account = 1234;
	checking.balance = 567.89;
	savings.account = 9876;
	savings.balance = 543.21;

	printf("Checking account %d has a balance of %f\n",
        checking.account,
        checking.balance
        );
	printf("Savings account %d has a balance of %f\n",
        savings.account,
        savings.balance
        );

	return(0);
}



const obj = {
    groceries: {
        cost: 33.22,
        amount: 1
    },
    rent: {
        cost: 899.00,
        amount: 1,
    },
    paycheck: {
        cost: -2000,
        amount: 2
    },
    restaurantBills: {
        cost: 20,
        amount: 4
    }
};

// Finish this:
const sum = Object.keys(obj)
	.filter(key => {
		return obj[key]['cost'] > 0;
	})
	.reduce((accumulated, currentVal) => {
		const cost = obj[currentVal].cost;
		const amount = obj[currentVal].amount;
		accumulated += (cost * amount);
		return accumulated;
	}, 0);

console.log(sum);
    
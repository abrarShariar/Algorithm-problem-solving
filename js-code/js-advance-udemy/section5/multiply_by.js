const multiplyBy = (multiplier) => {
	return function (num) {
		return multiplier * num;
	}
}

// const multiplyByTen = multiplyBy(10);
// const multiplyByTwenty = multiplyBy(20);
// console.log(multiplyByTwenty(5));
console.log(multiplyBy(12)(2));
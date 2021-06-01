const data = ['JavaScript', 'Python', 'C++', 'PHP'];
reducedData = data.reduce((accumulator, currentValue) => {
	accumulator += currentValue;
	// console.log(`Accumulator: ${accumulator}`);
	// console.log(`CurrentValue: ${currentValue}`);
	return accumulator;
}, "");

console.log(reducedData);


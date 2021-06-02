// filter out all the null values
const data = {
	name: 'Abrar',
	age: 100,
	skills: null,
	location: 'Tokyo, Japan',
	race: null
}

newObj = Object.keys(data)
	   .filter(key => data[key] != null)
	   .map(key => {
			return { [key]: data[key] };
	   });

// console.log(newObj);
const obj = {
    val1: 4,
    val2: 5,
    val3: 6,
};

const sum = Object.keys(obj)
	  .map(key => obj[key] * 3)
	  .reduce((accumulated, currentVal) => {
		accumulated += currentVal;
		return accumulated;
	  }, 0);

console.log(sum);
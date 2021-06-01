const obj = {
	name: 'Abrar'
};

obj.__proto__.sayMyName = function () {
	const name = "Shariar";
	console.log(this.name);
}

obj.__proto__.sayMyArrow = () => {
	const name = "Abrar";
	console.log(this.name);
}

// obj.sayMyName();
// // console.log(obj.__proto__);
// obj.sayMyArrow();

console.log(obj.hasOwnProperty('sayMyArrow'));
console.log(obj.hasOwnProperty('sayMyName'));
console.log(Object.getOwnPropertyNames(obj));
console.log(Object.getPrototypeOf(obj));


console.log(Object.getPrototypeOf(Array));
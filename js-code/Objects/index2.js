const obj1 = {
	name: 'Abrar Shariar',
	age: 24,
	address: 'Tokyo, Japan'
}

const obj2 = Object.assign({}, obj1);
console.log(obj2);

obj2.age = 50;

console.log(obj1);

const obj1 = {
	name: 'Abrar',
	age: 24,
	skills: ['python', 'JavaScript']
}

const obj2 = {
	name: 'Test',
	skills: ['C++', 'Java']
}

const newObj = Object.assign(obj2, obj1);
console.log(newObj);

newObj.name = 'TEST';

console.log(newObj);

obj1.age = 50;
console.log(newObj);



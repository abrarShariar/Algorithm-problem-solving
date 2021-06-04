let obj1 = {
	name: 'Abrar',
	age: 30
}

let obj2 = {
	name: 'Abrar',
	age: 30
}

console.log(Object.is(obj1, obj2));
console.log(Object.is(obj1, obj2));
console.log(Object.is(obj1, obj2));


obj1 = obj2;

console.log(Object.is(obj1, obj2));


// console.log(obj1 == obj2)

const a = 10;
const b = 10;

// console.log(a === b);
// console.log(a == b);

const l1 = [1,2,3]
const l2 = [1,2,3]

// console.log(l1 == l2);

// console.log(-1 === 1);
// console.log(Object.is(a));

const a1 = "Abrar";
const b1 = "Abrar";
// console.log(a1 === b1);
// console.log(Object.is(obj1, obj2));


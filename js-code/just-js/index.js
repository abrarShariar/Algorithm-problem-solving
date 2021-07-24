// var original = {
// 	title: 'Name',
// 	age: 20
// }
// function change(argOriginal) {
// 	var copy = {
// 		title: argOriginal.title,
// 		age: 20
// 	};
// 	copy.title = 'TEST';
// 	return copy;
// }

// var newCopy = change(original);
// console.log(newCopy);
// console.log(original)

// const person = {
// 	name: 'Abrar',
// 	skills: {
// 		title: 'C++'
// 	}
// }

// const personDup = {
// 	name: person.name,
// 	skills: person.skills
// }

// personDup.skills.title = 'Python'

// console.log(personDup);
// console.log(person);


const t1 = 10;
const t2 = {};
const t3 = [];
const t4 = '';
const t5 = null;
// const t6 = undefined;

console.log(typeof(t1));
// number

console.log(typeof(t2));
// object

console.log(typeof(t3));
// object

console.log(typeof(t4));
// object

console.log(typeof(t5));
// object

console.log(typeof(t6));
// undefined


const date = new Date();
console.log(typeof(date));


let st = 'abrar';
st[0] = '1';

// primitive values are immutable
console.log(typeof st);


let test = true; 
test.opp = false;
console.log(test.opp);

null = 10;
console.log(null);
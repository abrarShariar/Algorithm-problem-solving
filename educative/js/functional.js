// const x = 100;

// // function add (y) {
// // 	console.log(x + y);
// // }

// const add = (y) => {
// 	return x + y;
// }

// console.log(add(99));

function push10(arr) {
	arr.push(10);
}

arr = [];
obj = {}

// function mutateObj (in_obj) {
// 	in_obj.name = 'Abrar';
// }

const mutateObj = (in_obj) => {
	in_obj.name = 'Abrar';
}

const mutateName = (in_name) => {
	in_name = "No name";
}

console.log(arr);
push10(arr);
console.log(arr);

let name = "Abrar";
mutateName(name);

console.log(name);

mutateObj(obj);
console.log(obj);


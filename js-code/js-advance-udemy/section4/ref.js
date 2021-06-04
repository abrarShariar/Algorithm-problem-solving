const obj1 = {
	name: 'Abrar',
	value: 1
}

const obj2 = {
	name: 'Shariar',
	value: 2
}


function change(obj1, obj2) {
	obj1 = obj2;
	obj2.value = 9000;

	console.log(obj1, obj2);
}

console.log(obj1, obj2);
change(obj1, obj2);

console.log(obj1, obj2);



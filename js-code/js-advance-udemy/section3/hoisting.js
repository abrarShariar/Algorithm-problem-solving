
let a = 10;
// let a = 100;

// console.log(a);
var favFood = 'Grapes';
var foodForThoughts = function() {
	console.log(favFood);

	var favFood = 'Sushi';

	console.log(favFood);
}

// foodForThoughts();

function foo(name1, name2) {
	const [ n1, n2 ] = arguments;
	console.log(n1);
	console.log(n2);

	// console.log(arguments[0]);
}

foo("Abrar", "Shariar")
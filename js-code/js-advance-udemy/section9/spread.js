const animals = {
	tiger: 12,
	lion: 1,
	monkey: 12,
	skills: [1,2,3,4]
}

const { lion, ...rest } = animals;
// console.log(lion);
// console.log(rest);


function mySpread (...arr) {
	console.log(arr);
}

function getData ({ tiger, lion, skills }) {
	console.log(tiger, lion, skills);
}

const data = [1,2,3,4,5]
getData(animals);
const data = "New";
function level1() {
	const grandpa = 'grandpa';
	return function level2 () {
		const father = 'father';
		return function level3 () {
			const son = 'son';
			return function print_levels() {
				return `${data} ${grandpa} ${father} ${son}`;
			}
		}
	}
}

// console.log(level1()()()());
// memory efficient

function heavyArrayAction (index, fn) {
	const bigArray = new Array(index).fill('x');
	return fn(bigArray);
}

// heavyArrayAction(10, myfoo);

// encapsulation
const encapper = () => {
	let counter = 0;
	const secret = 'password';

	const increaseCounter = (incrementBy = 1) => {
		counter += incrementBy;
	}

	const showIncrementCount = () => {
		console.log(counter);
	}

	const destroyEncapper = () => {
		console.log("Destroying encapper");
	}

	const callDestroyer = (password) => {
		if (password === secret) {
			destroyEncapper();
		} else {
			console.log("OOPS wrong password");
		}
	}

	const pushMe = (pushBy = 1) => {
		increaseCounter(pushBy);
	}

	return {
		pushMe,
		callDestroyer,
		showIncrementCount
	}
}


const myEncapper = encapper();
// myEncapper.callDestroyer();
// myEncapper.destroyEncapper();
myEncapper.pushMe(1);
myEncapper.showIncrementCount();

myEncapper.pushMe(10);
myEncapper.showIncrementCount();




if (true) {
	var a = 1;
}

// function foo () {
// 	var a = 100;
// }

// const and let are block scoped variables.
// var is function scoped


// console.log(a);

function loop() {
	for (let i = 0; i < 5; i++) {
		console.log(i);
	}
	console.log("final", i);

}

// loop();
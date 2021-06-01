// (() => {
// 	console.log("Inside IIFE");
// 	const data = {
// 		name: "Abrar"
// 	}

// 	console.log(data);
// })();

// var i = 10;

// function myFoo () {
// 	console.log(i);
// }
// myFoo();

for (var i = 0; i < 3; i++) { // We are explicitly using `var` for a reason
	(function(i) {
		const time = i * 1000;
		setTimeout(function() {
			console.log(i);
		}, time);
	})(i);
}


// setTimeout() => i = 0, time = 0
// setTimeout() => i = 1, time = 1000
// setTimeout() => i = 2, time = 2000

// 0, 1, 


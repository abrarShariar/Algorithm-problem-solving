function hello_world(){
	// console.log(this);
	console.log(this.name);
	// console.log("Hello World");
	// console.log(this);
}

const obj = {
	name: 'Abrar',
	sayMyName: function () {
		console.log(this.name);
	}
}

const obj2 = {
	name: 'Cliff'
}

function fn () {
	console.log(this);
}

console.log(fn === window.fn);
// hello_world.apply(obj);
obj.sayMyName.call(obj2);
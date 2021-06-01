// class ArrowTest {}
// const car = new Car("My Car", "Toyota");
// console.log(car.name);
// console.log(car.brand);


// const Obj = {
// 	name: 'Abrar',
// 	sayMyName: () => {
// 		const name = "Asad";
// 		console.log(`My name is ${this.name}`);
// 	}
// }
// console.log(Obj.sayMyName());

// const myObject = {
// 	myMethod: () => {
// 		console.log(this);
// 	}
// };

// myObject.myMethod();

const obj = {
	value: 'abc',
	createArrowFn: () => {
		this.name = "Abrar";
		console.log(this);
	}
}

console.log(obj.createArrowFn());
// myarrow();
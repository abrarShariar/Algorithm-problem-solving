class Car {
	constructor(doors, engine, color) {
		this.doors = doors;
		this.engine = engine;
		this.color = color;
	}
}

class Toyota extends Car {
	constructor(doors, engine, color, speed = 10) {
		super(doors, engine, color);
		this.speed = speed;
	}
}

const civic = new Car(4, 'V6', 'Black');

const toy = new Toyota(1,'V8', 'Red');

console.log(toy);

// console.log(civic);
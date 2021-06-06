let carInstance = null;

class Car {
	constructor(name, type) {
		if (!carInstance) {
			this.name = name;
			this.type = type;
			carInstance = this;
		}
		return carInstance;
	}
}

const car1 = new Car('Abrar', 'Toyota');
const car2 = new Car('Asad', 'Toshiba');

console.log(car1);
console.log(car2);
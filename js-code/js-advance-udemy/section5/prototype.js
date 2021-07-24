const dragon = {
	name: 'Tanya',
	fight: true,
	fire: true,
	fire() {
		return `${this.name} is breathing fire!`
	},
	sing() {
		return `${this.name} is singing!`
	}
}

const lizard = {
	__proto__: dragon,
	lizz () {
		return `${this.name} is lizzing`
	},
	fight () {
		return `${this.name} cannot fight!`
	}
}

lizard.name = 'lizzi';

console.log(lizard);
console.log(lizard.lizz());
console.log(lizard.fight());

console.log(dragon.isPrototypeOf(lizard));
console.log(lizard.isPrototypeOf(dragon));
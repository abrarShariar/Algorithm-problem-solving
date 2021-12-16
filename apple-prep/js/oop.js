// class Car {
//     static carNumber = 0;
//     constructor(name = "My name", age = 100) {
//         this.name = name;
//         this.age = age;
//         Car.carNumber += 1;
//     }
//
//     // get name() {
//     //     console.log("Calling from get name!");
//     //     return this.name;
//     // }
//     //
//     // set name(name) {
//     //     console.log("Calling from the setter!");
//     //     this.name = name;
//     // }
// }
//
// const myCar = new Car();
// console.log(myCar.name);
// console.log(myCar.age)
//
// console.log(Car.carNumber);
// const myCar2 = new Car("Test", 123123);
// const myCar3 = new Car("Test2", 9999)
//
// console.log(Car.carNumber);
//
//
//

// const my_car = function my_car (name, color) {
//     this.name = name;
//     this.color = color;
//     this.sayMyCarName = function () {
//         console.log(`My Car name is ${this.name}`);
//     }
// };
//
// my_car.sayColorName = function () {
//     console.log(`My Car color is ${this.color}`);
// }
// let new_car = new my_car("Toyota", "Red");
// console.log(new_car.name);
// console.log(new_car.color)
// new_car.sayMyCarName();
// new_car.name = "BMW";
// new_car.sayMyCarName();
// new_car.sayColorName();

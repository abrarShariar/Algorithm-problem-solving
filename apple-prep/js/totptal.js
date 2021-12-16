// const test = {
//     name: "Hello World"
// }
// console.log(typeof test)
// console.log(typeof test === "object")
//
// console.log()
// console.log(toString.call(test))

// const test_name = {
//     // name: "Abrar",
//     age: 99
// }
//
// if (test_name['name']) {
//     console.log("Name key exists");
// } else {
//     console.log("No Name");
// }
//
//
// const arr = ['Abrar'];
// arr.push(100)
//
// console.log(arr)
// console.log(arr.shift());
//
// console.log(arr);
// console.log(arr.unshift(9000));
// console.log(arr);

// for (const key of Object.keys(test_name)) {
//     if (key) {
//
//     }
// }

// console.log(test_name)
// (function () {
//     let b = 10;
//     console.log(b);
// })();
//
// console.log(b);

const NameMasterClass = {
    name: ''
}

NameMasterClass.prototype.sayMyName = function sayMyName () {
    console.log(`My name is ${this.name}`);
}

const newName = NameMasterClass;
console.log(newName.name)

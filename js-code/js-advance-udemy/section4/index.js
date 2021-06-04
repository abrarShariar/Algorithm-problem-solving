const arr = [1,'A',90, true];
const obj = {
	'a': 1,
	'b': 2
}


// console.log(Array.isArray(arr));
// console.log(Array.isArray(obj));

// primitives are passed by value
// objects are passed by reference


const user = {
	name: 'Abrar',
	password: '1234'
}

// user_proto and user is pointing to the same memory in location
const user_proto = user;
user_proto.password = 'password';
console.log(user.password);

user.skills = ['JavaScript', 'Python']
console.log(user_proto.skills);

const my_list = [1,2,3,4,5]

// new_list and my_list both are pointing at the same location in memory
const new_list = my_list;

new_list.push(1000)
console.log(new_list);
console.log(my_list);


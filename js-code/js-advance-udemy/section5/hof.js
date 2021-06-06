const giveAccessTo = (name) => {
	return `Access Granted to ${name}`;
}

function authenticate (verify) {
	console.log("Inside authentication");
	let array = [];
	for (let i = 0; i < verify;i++) {
		array.push(i)
	}
}

function letUserLogin(username, auth) {
	auth(100000);
	return giveAccessTo(username);
}

const username = 'Abrar';
letUserLogin(username, authenticate)
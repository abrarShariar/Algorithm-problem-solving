const fetch = require('node-fetch');

const urls = [
	'https://jsonplaceholder.typicode.com/todos',
	'https://jsonplaceholder.typicode.com/posts',
	'https://jsonplaceholder.typicode.com/users'
];

allDataPromises = urls.map(url => {
	return fetch(url)
		.then(data => {
			console.log("found the data");
			return data.json();
		});
});

Promise.all(allDataPromises)
	.then(result => {
		console.log(result.length);
	})
	.catch(err => {
		console.log(err);
	});
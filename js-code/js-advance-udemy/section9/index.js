const promise = new Promise((resolve, reject) => {
	if (true) {
		resolve("Whooooo!");
	}
	reject("NOOOOOOO");
});

promise
	.then(data => {
		console.log(data);
		return 200;
	})
	.catch(err => {
		console.log("Any err", err);
	})
	.finally(() => {
		console.log("DONE!");
	});
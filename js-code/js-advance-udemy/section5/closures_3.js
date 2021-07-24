const array = [1,2,3,4];
for (let i = 0; i < array.length; i++) {
	setTimeout(() => {
		console.log(i);
	}, 2000)
}
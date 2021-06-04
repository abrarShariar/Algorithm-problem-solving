function foo1() {
	const a = 100;
	function foo2 () {
		console.log(a);
		console.log(b);
	}

	foo2();
}

function foo3 () {
	const b = 200;
	foo1();
}

const b = 300;
foo3();

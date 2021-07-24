function initializer () {
	let isInitialized = false;
	const initialize = () => {
		if (!isInitialized) {
			console.log("Initializing");
			isInitialized = true;
			console.log("Initialized");
			return;
		} 
		console.log("Already initialized!");
	}

	return {
		initialize
	}
}

const newInitializer = initializer();
newInitializer.initialize();
newInitializer.initialize();
newInitializer.initialize();



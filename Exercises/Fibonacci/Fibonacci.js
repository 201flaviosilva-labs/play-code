fibonacci();
function fibonacci() {
	console.log("-- Fibonacci --");

	const max = 100; // Max number to calculate
	let lastNumber = 0; // Last number, just a helper to calculate
	let currentNumber = 1; // The current number of the sequence

	while (currentNumber < max) {
		const next = currentNumber + lastNumber; // Helper variable
		lastNumber = currentNumber;
		currentNumber = next;
		console.log("Current number: " + currentNumber);
	}
}

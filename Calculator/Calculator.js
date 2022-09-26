const prompt = require("prompt-sync")(); // npm i prompt-sync

calculator();
function calculator() {
	console.log("-- Calculator --");
	console.log("[1] - Sum (+)");
	console.log("[2] - Sub (-)");
	console.log("[3] - Mult (*)");
	console.log("[4] - Div (/)");
	const operator = Number(prompt("Op: "));

	// Check if operator is permitted
	if (operator < 1 || operator > 4) {
		console.log("Error! Operator not permitted!");
		return;
	}

	const num1 = Number(prompt("Num 1: "));
	const num2 = Number(prompt("Num 2: "));

	switch (operator) {
		case 1:
			console.log(num1 + num2);
			break;
		case 2:
			console.log(num1 - num2);
			break;
		case 3:
			console.log(num1 * num2);
			break;
		case 4:
			console.log(num1 / num2);
			break;
		default:
			console.log("Error!");
	}
}

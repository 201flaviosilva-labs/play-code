const prompt = require("prompt-sync")(); // npm i prompt-sync

multiplicationTable();
function multiplicationTable() {
	console.log("-- Multiplication Table --");

	const times = 10;
	const num = Number(prompt("Number: "));

	for (let i = 0; i < times + 1; i++) {
		console.log(num + " * " + i + " = " + (i * num));
	}
}

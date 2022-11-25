const prompt = require("prompt-sync")(); // npm i prompt-sync

gradeAverage();
function gradeAverage() {
	console.log("-- Grade Average --");
	console.log("x - Stop add number and calculate de average");

	const values = [];
	let userValue;
	let index = 0;

	do {
		index++;
		userValue = prompt(`Value (${index}): `);
		if (userValue.toLowerCase() == "x") break;
		values.push(userValue);
	} while (userValue != "x");

	let sum = 0;
	values.map(v => { sum += Number(v); });

	console.log("Average: " + (sum / values.length));
}

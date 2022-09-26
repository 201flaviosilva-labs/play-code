const prompt = require("prompt-sync")(); // npm i prompt-sync

guessNumber();
function guessNumber() {
	console.log("-- Guess The Number --");

	const max = 100;
	let hideNumber = randomNumber(max);
	let playerTry;
	let attempts = 0;

	console.log("A number was hide between 0 and " + max);

	do {
		attempts++;
		playerTry = Number(prompt(attempts + " - Attempt: "));
		console.log("");
		checkAnswer(playerTry, hideNumber);
	} while (playerTry !== hideNumber);
}

function randomNumber(max) { return Math.floor(Math.random() * max + 1); }

function checkAnswer(playerTry, hideNumber) {
	if (playerTry === hideNumber) console.log("You found the number :)");
	else if (playerTry > hideNumber) console.log(`Your number(${playerTry}) it's to big.`);
	else if (playerTry < hideNumber) console.log(`Your number(${playerTry}) it's to low.`);
	else console.log("Error!");
}

const readline = require("readline").createInterface({
	input: process.stdin,
	output: process.stdout
});

// Intro
console.log("Lets play a game:");
console.log(" ---- Rock Paper Scissors ----");
console.log("");

console.log("Paper -> Rock");
console.log("Scissors -> Paper");
console.log("Rock -> Scissors");
console.log("");

// Player selection
readline.question("You: ", (player) => {
	if (player === "Rock" || player === "Paper" || player === "Scissors") {
		// Randomize CPU
		const rdn = Math.floor(Math.random() * 3);
		let cpu = "";

		if (rdn === 0) cpu = "Rock";
		else if (rdn === 1) cpu = "Paper";
		else cpu = "Scissors";

		console.log("CPU: " + cpu);

		// Check Winner
		console.log("");
		if (player === cpu) console.log("Draw");
		else if (
			(player === "Paper" && cpu === "Rock")
			|| (player === "Scissors" && cpu === "Paper")
			|| (player === "Rock" && cpu === "Scissors")
		) console.log("Player wins :)");
		else console.log("CPU wins :(");

	} else console.log("Option not available!");

	readline.close();
});

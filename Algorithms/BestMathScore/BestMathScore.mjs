// Run: node BestMathScore.js
// Run dev mode: node --watch BestMathScore.js

import fs from "node:fs";

class BestMathScore {
	constructor({
		numbers = [0, 1, 2, 3, 4, 5],
		operators = ["+", "-", "*", "/", "**", "%"],
		maxIterations = 100,
		repeatNumbers = true,
		maxEquationLength = numbers.length,
	}) {
		this.numbers = numbers;
		this.operators = operators;
		this.maxIterations = maxIterations;
		this.repeatNumbers = repeatNumbers;
		this.maxEquationLength = maxEquationLength;

		this.bestIteration = this._randomizeEquation();
		this.bestIterationResult = -Infinity;
		this.data = [];
		this.iteration = 0;
	}

	run() {
		do {
			this.iteration++;

			const { result, equation, equationString } = this.step();

			if (result > this.bestIterationResult) {
				this.bestIterationResult = result;
				this.bestIteration = equation;
			}

			const data = {
				iteration: this.iteration,
				result: result,
				current: equationString,
				bestResult: this.bestIterationResult,
				bestIteration: this._equationToString(this.bestIteration)
			};

			this.data.push(data);
			console.log(data);
		} while (this.iteration < this.maxIterations);

		console.log(`Best score: ${this.bestIterationResult} in ${this.iteration} iteration, equation: ${this._equationToString(this.bestIteration)}`);
	}

	step() {
		const equation = this._randomizeEquation();

		const equationString = this._equationToString(equation);


		const result = eval(equationString);

		if (result === Infinity || result === NaN) return -Infinity;
		return { result, equation, equationString };
	}

	export() {
		fs.writeFileSync("data.json", JSON.stringify(this.data));
	}

	_randomizeEquation() {
		const numbers = [...this.numbers];
		const operators = [...this.operators];
		const equation = [];

		for (let i = 0; i < this.maxEquationLength; i++) {
			let randomNumber;
			do {
				randomNumber = Math.floor(Math.random() * numbers.length);
				if (this.repeatNumbers || (!this.repeatNumbers && !equation.includes(numbers[randomNumber]))) break;
			} while (true);

			equation.push(numbers[randomNumber]);

			const randomOperator = Math.floor(Math.random() * operators.length);
			equation.push(operators[randomOperator]);
		}

		equation.pop();

		return equation;
	}

	_equationToString(equation) {
		return equation.toString().replace(/\,/g, "");
	}
}

const best = new BestMathScore({
	maxIterations: 100000,
	repeatNumbers: true,
});
best.run();
// best.export();

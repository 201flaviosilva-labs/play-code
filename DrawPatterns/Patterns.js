function box(lines = 10, columns = 10) {
	let result = "";
	for (let i = 0; i < lines; i++) {
		for (let j = 0; j < columns; j++) {
			if (i === 0 || i === lines - 1 || j === 0 || j === columns - 1) result += "X"
			else result += " "
		}
		result += "\n";
	}
	return result;
}

function boxX(lines = 10, columns = 10) {
	let result = "";
	for (let i = 0; i < lines; i++) {
		for (let j = 0; j < columns; j++) {
			if (i === 0 || i === lines - 1 ||
				j === 0 || j === columns - 1 ||
				i === j || i + j === lines) result += "X"
			else result += " "
		}
		result += "\n";
	}
	return result;
}

function xLines(lines = 10, columns = 10) {
	let result = "";
	for (let i = 0; i < lines; i++) {
		for (let j = 0; j < columns; j++) {
			if (i === j || i + j === lines) result += "X"
			else result += " "
		}
		result += "\n";
	}
	return result;
}

function triangle1(lines = 10) {
	let result = "";
	for (let i = 0; i < lines; i++) {
		for (let j = 0; j < i; j++) {
			result += "X";
			if (j < i - 1) result += " ";
		}
		result += "\n";
	}

	return result;
}

function triangle2(lines = 10) {
	let result = "";
	for (let i = lines; i > 0; i--) {
		for (let j = i; j > 0; j--) {
			result += "X";
			if (j > 1) result += " ";
		}
		result += "\n";
	}
	return result;
}

function triangle3(lines = 10) {
	let result = "";
	for (let i = lines; i > 0; i--) {
		for (let j = 0; j < lines; j++) {
			if (j > i) result += "X";
			result += " ";
		}
		result += "\n";
	}
	return result;
}

function triangle4(lines = 10) {
	let result = "";
	for (let i = 0; i < lines; i++) {
		for (let j = 0; j < lines; j++) {
			if (j > i) result += "X";
			result += " ";
		}
		result += "\n";
	}
	return result;
}

console.log(box(10, 10));
console.log(boxX(15, 15));
console.log(xLines(15, 20));

console.log(triangle1(20));
console.log(triangle2(20));
console.log(triangle3(20));
console.log(triangle4(20));

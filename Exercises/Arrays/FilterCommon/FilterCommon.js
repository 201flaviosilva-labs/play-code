console.log(filterCommon(["A", "B", "C", "D"], ["B", "D", "F", "H"])); // "B", "D"

function filterCommon(arr1, arr2) {
	const result = [];

	for (let i = 0; i < arr1.length; i++) {
		for (let j = 0; j < arr2.length; j++) {
			if (arr1[i] === arr2[j]) {
				result.push(arr1[i]);
				break;
			}
		}
	}

	return result;
}

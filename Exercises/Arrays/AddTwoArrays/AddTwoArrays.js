console.log(addTowArrays([1, 2, 3, 4], [5, 6, 7, 8])); // [6,8,10,12]

function addTowArrays(arr1, arr2) {
	const result = [];

	for (let i = 0; i < arr1.length; i++) {
		result.push(arr1[i] + arr2[i]);
	}

	return result;
}

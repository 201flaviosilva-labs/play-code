console.log(removeDuplicates([2, 1, 1, 3, 2, 7, 2, 3, 8, 0])); // 2,1,3,7,8

function removeDuplicates(arr) {
	const newArray = [];

	for (let i = 0; i < arr.length; i++) {
		let contains = false;
		for (let j = 0; j < newArray.length; j++) {
			if (arr[i] === newArray[j]) {
				contains = true;
				break;
			}
		}
		if (!contains) newArray.push(arr[i]);
	}

	return newArray;
}

function isSorted(arr = []) {
	for (let i = 0; i < arr.length - 1; i++) {
		if (arr[i] > arr[i + 1]) return false;
	}
	return true;
}

/**
 * Sort given array using the Selection Sort algorithm
 * @see {@link https://pt.wikipedia.org/wiki/Bogosort}
 * 
 * @param {number[]} arr - The array to sort
 * @returns {number[]} the given array, sorted using the Selection Sort algorithm
 * 
 * @function bogoSort
 */
function bogoSort(arr) {
	while (!isSorted(arr)) {
		arr.sort(() => Math.random() - 0.5);
	}

	return arr;
}

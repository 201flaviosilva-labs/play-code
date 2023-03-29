/**
 * Sort given array using the Selection Sort algorithm
 * @see {@link https://www.geeksforgeeks.org/selection-sort/}
 * 
 * @param {number[]} arr - The array to sort
 * @returns {number[]} the given array, sorted using the Selection Sort algorithm
 * @function selectionSort
 */
function selectionSort(arr) {
	for (let i = 0; i < arr.length; i++) {
		let low = arr[i];
		let index = i;

		for (let j = i + 1; j < arr.length; j++) {
			if (arr[j] < low) {
				low = arr[j];
				index = j;
			}
		}

		if (low !== arr[i]) {
			arr[index] = arr[i];
			arr[i] = low;
		}
	}

	return arr;
}

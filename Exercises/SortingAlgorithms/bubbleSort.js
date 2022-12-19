/**
 * Sort given array using the Bubble Sort algorithm
 * @see {@link https://pediaa.com/what-is-the-difference-between-bubble-sort-and-selection-sort/}
 * 
 * @param {number[]} arr - The array to sort
 * @returns {number[]} the given array, sorted using the Bubble Sort algorithm
 * @function bubbleSort
 */
function bubbleSort(arr) {
	for (let i = 0; i < arr.length - 1; i++) {
		for (let j = 0; j < arr.length - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				const temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

	return arr;
}

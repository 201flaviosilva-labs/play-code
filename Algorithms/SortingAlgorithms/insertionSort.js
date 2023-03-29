/**
 * Sort given array using the Insertion Sort algorithm
 * @see {@link https://en.wikipedia.org/wiki/Insertion_sort}
 * 
 * @param {number[]} arr - The array to sort
 * @returns {number[]} the given array, sorted using the Insertion Sort algorithm
 * @function insertionSort
 */
function insertionSort(arr) {
	for (let i = 0; i < arr.length; i++) {
		const current = arr[i];

		for (let j = i - 1; j >= 0; j--) {

			if (arr[j + 1] < arr[j]) {
				arr.splice(j + 1, 1);
				arr.splice(j, 0, current);
			}
		}
	}

	return arr;
}

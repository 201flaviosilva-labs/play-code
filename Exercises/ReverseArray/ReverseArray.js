console.log(reverseSameArray([0, 1, 2, 3])); // 3,2,1,0
console.log(reverseNewArray([0, 1, 2, 3])); // 3,2,1,0

function reverseSameArray(arr) {
  const size = Math.floor(arr.length / 2);

  for (let i = 0; i < size; i++) {
    const index = arr.length - i - 1;
    const tempValue = arr[index];
    arr[index] = arr[i];
    arr[i] = tempValue;
  }
}

function reverseNewArray(arr) {
  const reversedArray = [];

  for (let i = 0; i < arr.length; i++) {
    const index = arr.length - i - 1;
    reversedArray[i] = arr[index];
  }

  return reversedArray;
}

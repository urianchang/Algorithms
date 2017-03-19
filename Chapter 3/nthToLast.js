/*
Array: Nth-to-Last

Return the element that is N-from-array's-end.
*/

function nLast(arr, num) {
  if (num > arr.length) {
    return null;
  }
  return arr[arr.length-num];
}

var arr1 = [5, 2, 3, 6, 4, 9, 7];
console.log(nLast(arr1, 3));
console.log(nLast(arr1, 8));

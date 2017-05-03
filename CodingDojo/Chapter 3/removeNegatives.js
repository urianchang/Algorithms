/*
Array: Remove Negatives

Implement removeNegatives() that accepts an array, removes negative
values, and returns the same array (not a copy), preserving
non-negatives' order. As always, do not use built-in array functions.
*/

function remNeg(arr) {
  for (var i = arr.length-1; i >= 0; i--) {
    if (arr[i] < 0) {
      for (var idx = i; idx < arr.length-1; idx++) {
        var temp = arr[idx];
        arr[idx] = arr[idx+1];
        arr[idx+1] = temp;
      }
      arr.pop()
    }
  }
  return arr;
}

var arr1 = [-3, 0, 1, -5, 2, -1, 3, 4];
console.log(remNeg(arr1));

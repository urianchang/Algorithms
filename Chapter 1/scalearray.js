// Scale the array
// Given an array arr and a number num, multiply
// all values in arr by num, and return the changed
// array arr.

function scale(arr, num) {
  for (var x = 0; x < arr.length; x++) {
    arr[x] *= num;
  }
  return arr;
}

var a = [1, 2, 3, 4];
var b = 10;
console.log(scale(a, b));

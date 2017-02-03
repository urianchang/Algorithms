// Reverse Array
// Given array, write a function that reverses values, in-place.

function reverse(arr) {
  for (var i = 0; i < arr.length/2; i++) {
    var temp = arr[i];
    arr[i] = arr[arr.length - 1 - i];
    arr[arr.length-1-i] = temp;
  }
  return arr;
}

a = [3, 1, 6, 4, 2];
console.log(reverse(a));

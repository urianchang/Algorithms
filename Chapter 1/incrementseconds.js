// Increment the Seconds
// Given an array of numbers, arr, add 1
// to every second element, specifically those
// whose index is odd. Afterward, console.log
// each array value and return arr.

function increment(arr) {
  for (var x = 0; x < arr.length; x++) {
    if (x%2 != 0) {
      arr[x] += 1;
    }
    console.log(arr[x]);
  }
  return arr;
}

var a = [1, 2, 3, 8 ,4, 5, 6];
console.log(increment(a));

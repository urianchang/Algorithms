// Countdown
// Create a function that accepts a number as an input.
// Return a new array that counts down by one, from the number
// (as array's zero'th element) down to 0 (as the last element).
// How long is this array?

function countdown(num) {
  var arr = [];
  for (var x = num; x >= 0; x--) {
    arr.push(x);
  }
  return arr;
}

var arr = countdown(3);
console.log(arr.length);

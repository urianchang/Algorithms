// Print Low, Return High
// Create a function that takes array of numbers.
// The function should print the lowest value in the array,
// and return the highest value in the array.

function doit(arr) {
  var low = arr[0];
  var high = arr[0];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < low) {
      low = arr[i];
    }
    if (arr[i] > high) {
      high = arr[i];
    }
  }
  console.log(low);
  return high;
}

a = [1, 2, 3, 4, 5];
console.log(doit(a));

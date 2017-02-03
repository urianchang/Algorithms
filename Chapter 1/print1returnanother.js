// Print One, Return Another
// Build a function that takes array of numbers. The function
// should print second-to-last value in the array, and return
// first odd value in the array.

function panth (arr) {
  console.log("Second to last value: " + arr[arr.length - 2]);
  for (var i = 0; i < arr.length; i++) {
    if (arr[i]%2 != 0) {
      return arr[i];
    }
  }
  return "No odd numbers in the array";
}

a = [2, 3, 4, 5, 7];
b = [2, 4, 6];
console.log(panth(a));
console.log(panth(b));

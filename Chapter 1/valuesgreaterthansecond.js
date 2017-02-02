// Values Greater Than second
// For [1, 3, 5, 7, 9, 13], print values greater than its 2nd value.
// Return how many values this is.

function valuesgreater(arr) {
  var count = 0;
  for (var x = 0; x < arr.length; x++) {
    if (arr[x] > arr[1]) {
      console.log(arr[x]);
      count++
    }
  }
  return count;
}

a = [1, 3, 5, 7, 9, 13];
console.log(valuesgreater(a));

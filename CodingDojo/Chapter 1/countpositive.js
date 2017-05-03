// Count Positive
// Given array of numbers, create function to replace last value
// with number of positive values.

function positive(arr) {
  var count = 0;
  for (var x = 0; x < arr.length; x++) {
    if (arr[x] > 0) {
      count++;
    }
  }
  arr[arr.length-1] = count;
  return arr;
}

a = [-1, 1, 1, 1];
console.log(positive(a));

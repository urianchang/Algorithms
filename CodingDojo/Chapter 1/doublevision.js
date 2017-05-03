// Double Vision
// Given array, create a function to return a new
// array where each value in the original has been
// doubled.

function double(arr) {
  var newarr = [];
  for (var x = 0; x < arr.length; x++) {
    newarr.push(arr[x]*2);
  }
  return newarr;
}

a = [1, 2, 3];
console.log(double(a));

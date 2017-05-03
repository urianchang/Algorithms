// Add Seven to Most
// Build function that accepts array. Return a new array
// with all values except first, adding 7 to each. Do not
// alter the original array.

function add7 (arr) {
  var newarr = [];
  for (ind = 1; ind < arr.length; ind++) {
    newarr.push(arr[ind]+7);
  }
  return newarr;
}

a = [1, 2, 3, 4];
console.log(add7(a));

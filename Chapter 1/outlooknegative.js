// Outlook: Negative
// Given an array, create and return a new one
// containing all the values of the provided array,
// made negative (not simply multiplied by -1).

function neg(arr) {
  var newarr = [];
  for (var x = 0; x < arr.length; x++) {
    if (arr[x] > 0) {
      newarr.push(arr[x] * -1);
    } else {
      newarr.push(arr[x]);
    }
  }
  return newarr;
}

a = [1, -3, 5];
console.log(neg(a));

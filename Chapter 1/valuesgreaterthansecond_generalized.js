// Values Greater than Second, Generalized
// Write a function that accepts any array, and returns
// a new array with the array values that are Greater
// than its 2nd value. Print how many values this is.
// What will you do if the array is only one element long?

function valuable(arr) {
  if (arr.length <= 1) {
    console.log("ERROR: There's only one element in this array");
    return -1;
  } else {
    var newarr = [];
    for (var x = 0; x < arr.length; x++) {
      if (arr[x] > arr[1]) {
        newarr.push(arr[x]);
      }
    }
    return newarr;
  }
}

a = [2, 4, 6, 7, -1];
b = [1];
console.log(valuable(a));
console.log(valuable(a).length);
console.log(valuable(b));

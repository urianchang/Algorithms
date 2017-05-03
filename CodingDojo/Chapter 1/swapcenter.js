// Swap Toward the Center
// Given array, swap first and last, third and third-to-last, etc.

function swap(arr) {
  for (var x = 0; x < arr.length/2; x+=2) {
    var temp = arr[x];
    arr[x] = arr[arr.length-1-x];
    arr[arr.length-1-x] = temp;
  }
  return arr;
}

var a = [true, 42, "Ada", 2, "pizza"];
var b = [1, 2, 3, 4, 5, 6];
console.log(swap(a));
console.log(swap(b));

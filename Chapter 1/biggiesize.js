// Biggie Size
// Given an array, write a function that changes all
// positive numbers in the array to "big".

function makeItBig(arr) {
  for (var ind = 0; ind < arr.length; ind++) {
    if (arr[ind] > 0) {
      arr[ind] = "big";
    }
  }
  return arr;
}

ar = [-1, 3, 5, -5]

console.log(makeItBig(ar));

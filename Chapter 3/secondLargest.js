/*
Array: Second-Largest

Return the second-largest element of an array.
*/

function secondLargest(arr) {
  if (arr.length < 2) {
    return null;
  } else {
    var L, secondL;
    if (arr[0] > arr[1]) {
      L = arr[0];
      secondL = arr[1];
    } else {
      L = arr[1];
      secondL = arr[0];
    }
    for (var i = 2; i < arr.length; i++) {
      if (arr[i] > L) {
        secondL = L;
        L = arr[i];
      } else if (arr[i] > secondL) {
        secondL = arr[i];
      }
    }
  }
  return secondL;
}

var arr1 = [42, 1, 4, Math.PI, 7];
var arr2 = [3];
console.log(secondLargest(arr1));
console.log(secondLargest(arr2));

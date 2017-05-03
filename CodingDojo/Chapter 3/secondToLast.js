/*
Array: Second-to-Last

Return the second-to-last element of an array.
*/

function secondLast(arr) {
  if (arr.length < 2) {
    return null;
  }
  return arr[arr.length-2];
}

var arr1 = [42, true, 4, "Liam", 7];
var arr2 = [10];
console.log(secondLast(arr1));
console.log(secondLast(arr2));

/*
Balance Index:

Here, a balance point is on an index, not between indices.
Return the balance index, where sums are equal on either side.
Return -1 if none exist.
*/

//: Similar solution as Balance Point, but do the summing from left at end of the loop
function balIndex (arr) {
  // 1. Get total sum of the array
  var sumTotal = arr[0];
  for (var i = 1; i < arr.length; i++) {
      sumTotal += arr[i];
  }
  // 2. Start adding from left and remove each value from total sum
  var sumLeft = 0;
  for (var idx = 0; idx < arr.length; idx++) {
      sumTotal -= arr[idx];
      if (sumLeft == sumTotal) {
          return idx;
      }
      sumLeft += arr[idx];
  }
  return -1;
}


var arr1 = [-2, 5, 7, 0, 3];    //: 2
var arr2 = [9, 9];      //: -1
var arr3 = [3, -2, 0, 4, 6, -5];    //: 3
console.log(balIndex(arr3));

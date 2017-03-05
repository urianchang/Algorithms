/*
Book Index

Given a sorted array of pages where a term appears,
produce an index string. Consecutive pages should
form ranges separated by a hyphen.

For [1, 13, 14, 15, 37, 38, 70], return string
"1, 13-15, 37-38, 70".
*/

function bookSort(arr) {
  var ind = 0;
  var strArr = [];
  var numRange = [];
  while (ind < arr.length) {
    if (arr[ind+1] != arr[ind]+1) {
      if (numRange.length == 0) {
        strArr.push(arr[ind]);
      } else {
        strArr.push(numRange[0]+"-"+numRange[numRange.length-1]);
        numRange = [];
      }
    } else {
      numRange.push(arr[ind]);
      numRange.push(arr[ind+1]);
    }
    ind++;
  }
  return strArr.join(", ");
}

var arr1 = [1, 13, 14, 15, 37, 38, 70];
console.log(bookSort(arr1));

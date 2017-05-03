/*
Array: Number of Values (without .Length)

Without using the .length property that is present on all arrays,
determine and return the number of values in the given array.
*/

function countAA(assocArr) {
  var count = 0;
  for (key in assocArr) {
    count++;
  }
  return count;
}

var arr1 = {band: "Travis Shredd", style: "Country", album: "668"};
console.log(countAA(arr1));

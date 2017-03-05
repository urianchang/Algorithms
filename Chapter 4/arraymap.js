/*
Zip Arrays into Map

Associative arrays are sometimes called maps because
a key (string) mapts to a value. Given two arrays,
create an associate array (map) containing keys of the first,
and values of the second.
*/

function zipArrs(arr1, arr2) {
  var assocArr = {};
  for (var ind = 0; ind < arr1.length; ind++) {
    assocArr[arr1[ind]] = arr2[ind];
  }
  return assocArr;
}

var arr1 = ["abc", 3, "yo"];
var arr2 = [42, "wassup", true];
console.log(zipArrs(arr1, arr2));

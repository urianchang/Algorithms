/*
Invert Hash

Associative arrays are also called hashes.
Build invertHash(assocArr) to convert hash keys
to values, and values to keys.
*/

function invertHash(assocArr) {
  var newAssocArr = {};
  for (key in assocArr) {
    newAssocArr[assocArr[key]] = key;
  }
  return newAssocArr;
}

var assocArr1 = {"name": "Zaphod", "charm": "high", "morals": "dicey"};
console.log(invertHash(assocArr1));

/*
Remove array duplicates. Do not alter original.
Return new array with results 'stable' (original
order). For [1, 2, 1, 3, 4, 2] return [1, 2, 3, 4]
*/

function removeDupes(array) {
  var new_array = [];
  var is_dupe = false;
  for (var i=0; i < array.length; i++) {
    for (var j=0; j < new_array.length; j++) {
      if (array[i] == new_array[j]) {
        is_dupe = true;
        break;
      }
    }
    if (is_dupe == false) {
      new_array.push(array[i]);
    }
    is_dupe = false;
  }
  return new_array;
}

//: Work 'in-place' in a given array.
//: Use a hash table to track values.
//: Return stable array.
function removeDupes_hash(array) {
  var hash = {};
  var idx = 0;
  while (idx < array.length) {
    if (array[idx] in hash) {
      array.splice(idx, 1);
    } else {
      hash[array[idx]] = 1;
    }
    idx++;
  }
  return array;
}


var og = [1, 2, 1, 3, 4, 2];
console.log(removeDupes(og));
console.log(removeDupes_hash(og));

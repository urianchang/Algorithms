/*
Array: flatten

Flatten a given array, eliminating nested & empty arrays.
Do not alter it; return a new one retaining order.

Second: work 'in-place' in the given array (do not create
another). Alter order if needed.

Third: make your algorithm both in-place and stable.
*/

// Helper function for inserting value at index in array
function insertAt(arr, val, idx) {
  arr[arr.length] = val;
  for (var x = arr.length-1; x > idx; x--) {
    var temp = arr[x];
    arr[x] = arr[x-1];
    arr[x-1] = temp;
  }
}

// Helper function for removing value at index in array
function removeAt(arr, idx) {
        var val = arr[idx];
        for (var i=idx; i < arr.length-1; i++) {
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
        arr.pop();
        return val;
}

// Main function (level 3)
function flatten(arr) {
  if (Array.isArray(arr)) {
    var i = 0;
    while (i < arr.length) {
      if (Array.isArray(arr[i])) {
        var inArr = arr[i];
        for (var j = inArr.length-1; j >= 0; j--) {
          insertAt(arr, inArr[j], i);
        }
        removeAt(arr, i+inArr.length);
      } else {
        i++;
      }
    }
  }
  return arr;
}

var arr1 = [1, 2, 3, [4, 5, [6, 7, 8]], 9];
console.log(flatten(arr1)); //[1, 2, 3, 4, 5, 6, 7, 8, 9]

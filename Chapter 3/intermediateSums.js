/*
Intermediate Sums

You will be given an array of numbers. After every tenth
element, add an additional element containing the sum
of those values. If the array does not end aligned evenly
with ten elements, add one last sum that includes those
last elements not yet been included in one of the earlier
sums.
*/

function interSums(arr) {
    var idx = 0;
    var sum = 0;
    while (idx < arr.length) {
        if ((idx+1) % 11 == 0) {
            insertAt(arr, idx, sum);
            sum = 0;
            idx++;
        } else {
            sum += arr[idx];
            idx++;
        }
    }
    if ((idx+1) % 11 != 0) {
        arr.push(sum);
    }
    return arr;
}

//: Helper function for inserting value into array at given index
function insertAt(arr, ind, val) {
    arr[arr.length] = val;
    for (var x = arr.length-1; x > ind; x--) {
        var temp = arr[x];
        arr[x] = arr[x-1];
        arr[x-1] = temp;
    }
    return arr;
}

var arr1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2];
console.log(interSums(arr1));

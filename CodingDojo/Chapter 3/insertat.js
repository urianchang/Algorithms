/*
Array: Insert At

Given array, index, and additional value, insert the value into array at given index.
Do this without using built-in array methods. You can think of pushFront(arr, val)
as equivalent to insertAt(arr, 0, val).
*/

function insertAt(arr, ind, val) {
    arr[arr.length] = val;
    for (var x = arr.length-1; x > ind; x--) {
        var temp = arr[x];
        arr[x] = arr[x-1];
        arr[x-1] = temp;
    }
    return arr;
}

var arr1 = [1, 2, 3, 4, 5]
console.log(insertAt(arr1, 2, 4));

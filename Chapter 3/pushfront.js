/*
Array: Push Front
Given array and an additional value, insert this value at the beginning
of the array. Do this without using any built-in array methods.
*/

function pushF(arr, value) {
    arr[arr.length] = value;
    for (var x = arr.length-1; x > 0; x--) {
        temp = arr[x];
        arr[x] = arr[x-1];
        arr[x-1] = temp;
    }
    return arr;
}

var arr = [1, 2, 3]
var value = 4
console.log(pushF(arr, value));

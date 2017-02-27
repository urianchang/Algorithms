/*
Array: Min to Front

Given an array of comparable values, move the lowest element to array's front,
shifting backward any elements previously ahead of it. Do not otherwise change
the array's order. Given [4, 2, 1, 3, 5], change it to [1, 4, 2, 3, 5] and return it.
*/

function minToFront(arr) {
    var min = arr[0];
    var idx = 0;
    for (var i = 1; i < arr.length; i++){
        if (arr[i] < min) {
            min = arr[i];
            idx = i;
        }
    }
    for (var x = idx; x > 0; x--){
        var temp = arr[x];
        arr[x] = arr[x-1];
        arr[x-1] = temp;
    }
    return arr;
}

var arr1 = [4, 2, 1, 3, 5];
var arr2 = [2, 3, 5, 6, 7, 8, 1, 10, 9];
console.log(minToFront(arr1));
console.log(minToFront(arr2));

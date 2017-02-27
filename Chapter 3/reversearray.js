/*
Array: Reverse

Given a numerical array, reverse the order of values, in-place.
*/

function reverseArr(arr) {
    for (var i = 0; i < arr.length/2; i++) {
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    return arr;
}

var arr1 = [1, 2, 3, 4, 5];
var arr2 = [1, 2, 3, 4, 5, 6];
console.log(reverseArr(arr1));
console.log(reverseArr(arr2));

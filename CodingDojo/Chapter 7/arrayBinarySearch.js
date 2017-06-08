/*
Array: Binary Search

Given a sorted array and a value, return whether the array
contains that value. Do not sequentially iterate the array.
Instead, 'divide and conquer', taking advantage of the fact
that the array is sorted. As always, only use built-in functions
that you are prepared to recreate (write yourself) on demand!
*/

function search(arr, val) {
    if (val > arr[arr.length - 1] || val < arr[0]) {
        return false;
    }
    return binarySearch(arr, val);
}

function binarySearch(arr, val) {
    var mid = Math.floor(arr.length/2);
    // console.log(mid);
    if (arr.length === 1) {
        return arr[0] === val;
    }
    if (val >= arr[mid]) {
        // console.log("greater");
        return binarySearch(arr.slice(mid), val);
    }
    if (val < arr[mid]) {
        // console.log("less than");
        return binarySearch(arr.slice(0, mid), val);
    }
    return false;
}

var arr1 = [1, 2, 3, 4, 5, 6];
var arr2 = [1, 2, 3, 4, 5];
console.log(search(arr1, 4.5)); // false

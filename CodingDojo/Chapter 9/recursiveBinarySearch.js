/*
Recursive Binary Search:

Given a sorted array and a value, recursively determine
whether value is found within array.
*/

function rBS(arr, val) {
    //: Find middle index of array
    var mid = Math.floor(arr.length / 2);
    //: If middle value is search value...
    if (arr[mid] === val) {
        return true;
    //: If search value is less than middle value...
    } else if (val < arr[mid] && arr.length > 1) {
        return rBS(arr.slice(0, mid), val);
    //: If search value is greater than middle value...
    } else if (val > arr[mid] && arr.length > 1) {
        return rBS(arr.slice(mid, arr.length), val);
    //: If search value doesn't exist in array...
    } else {
        return false;
    }
}

console.log(rBS([1, 3, 5, 6], 4));  // false
console.log(rBS([4, 5, 6, 8, 12], 5));  // true
console.log(rBS([1, 2, 3, 4, 5], 8));  // false
console.log(rBS([4, 5, 8, 12], 12)); // true

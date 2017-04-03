/*
Balance Point:

Write a function that returns whether the given array
has a balance point between indices, where one side's sum
is equal to the other's.
*/

function balPoint(arr) {
    // 1. Get total sum of the array
    var sumTotal = arr[0];
    for (var i = 1; i < arr.length; i++) {
        sumTotal += arr[i];
    }
    // 2. Start adding from left and subtract each value from total sum
    var sumLeft = 0;
    for (var idx = 0; idx < arr.length; idx++) {
        sumTotal -= arr[idx];
        sumLeft += arr[idx];
        if (sumLeft == sumTotal) {
            return true;
        }
    }
    return false;
}

var arr1 = [1, 2, 3, 4, 10];  //: true
var arr2 = [1, 2, 3, 2, 1];   //: false
var arr3 = [-1, 3, 1, 1];   //: true
console.log(balPoint(arr1));
console.log(balPoint(arr2));
console.log(balPoint(arr3));

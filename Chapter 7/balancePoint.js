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
    // 2. Start adding from left and compare with half of total sum
    var sumLeft = arr[0];
    for (var idx = 1; idx < arr.length; idx++) {
        sumLeft += arr[idx];
        if (sumLeft == sumTotal/2) {
            return true;
        }
        if (sumLeft > sumTotal/2) {
            return false;
        }
    }
}

var arr1 = [1, 2, 3, 4, 10];
var arr2 = [1, 2, 3, 2, 1];
console.log(balPoint(arr1));
console.log(balPoint(arr2));

/*
Max/Min/Average with Object

Given an array, return an object containing
the array's max, min, and average values.
*/

function objectify(arr) {
    let obj = {
        min: arr[0],
        max: arr[0],
        avg: arr[0]
    }
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < obj.min) {
            obj.min = arr[i];
        }
        if (arr[i] > obj.max) {
            obj.max = arr[i];
        }
        obj.avg += arr[i];
    }
    obj.avg = obj.avg / arr.length;
    return obj
}

var arr1 = [1, 2, 3, 4, 5];
console.log(objectify(arr1));   //: { min: 1, max: 5, avg: 3 }
var arr2 = [100, 50, 0];
console.log(objectify(arr2));   //: { min: 0, max: 100, avg: 50 }
var arr3 = [2, 4, 6, 8, 10, 12];
console.log(objectify(arr3));   //: { min: 2, max: 12, avg: 7 }

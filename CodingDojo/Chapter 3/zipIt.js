/*
Zip It

Create a standalone function that accepts two arrays
and combines their values sequentially into a new
array, at alternating indices starting with first array.
Extra values from either array should be included afterward.
*/

function zip(a1, a2) {
    var newArr = [];
    var count = (a1.length > a2.length ? a1.length : a2.length);
    for (var i = 0; i < count; i++) {
        if ( i < a1.length ) {
            newArr.push(a1[i]);
        }
        if ( i < a2.length ) {
            newArr.push(a2[i]);
        }
    }
    return newArr;
}

var arr1 = [1, 2];
var arr2 = [10, 20, 30, 40];
console.log(zip(arr1, arr2)); //: [1, 10, 2, 20, 30, 40]

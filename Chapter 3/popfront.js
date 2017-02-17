/*
Array: Pop Front
Given array, remove and return the value at the beginning of the array.
Do this without using any built-in array methods except pop().
*/

function popFront(arr) {
    var temp = arr[0];
    for (var x = 0; x < arr.length-1; x++){
        var swap = arr[x];
        arr[x] = arr[x+1];
        arr[x+1] = swap;
    }
    arr.pop();
    return temp;
}

var arr = [5, 6, 7, 8];
console.log(popFront(arr));
console.log(arr);

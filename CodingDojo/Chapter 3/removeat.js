/*
Array: Remove At

Given array and an index into array, remove and return the array value
at that index. Do this without using any built-in array methods
except pop(). Think of popFront(arr) as equivalent to removeAt(arr, 0).
*/

function removeAt(arr, idx) {
        var val = arr[idx];
        for (var i=idx; i < arr.length-1; i++) {
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
        arr.pop();
        return val;
}

var arr1 = [1, 2, 3, 4, 5];
console.log(removeAt(arr1, 2));
console.log(arr1);

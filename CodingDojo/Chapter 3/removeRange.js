/*
Array: Remove Range

Given array, and indices 'start' and 'end,' remove
vals in that index range, working in-place (hence
shortening the array).

*/

function removeRange(arr, start, end) {
    for (var count = 0; count < (end - start + 1); count++) {
        removeAt(arr, start);
    }
    return arr;
}

//: Helper function for removing array element at index
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

var arr1 = [20, 30, 40, 50, 60, 70];
console.log(removeRange(arr1, 2, 4));

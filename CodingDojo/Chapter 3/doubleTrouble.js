/*
Double Trouble

Create a function that changes a given array to list each existing
element twice, retaining orginal order.
*/

function double(arr) {
    var count = arr.length;
    for (var i = count-1; i >= 0; i--) {
        // console.log(i, arr, arr[i]);
        arr.push(arr[i]);
        for (var idx = arr.length-1; idx > i+1; idx--) {
            // console.log(idx);
            var temp = arr[idx];
            arr[idx] = arr[idx-1];
            arr[idx-1] = temp;
        }
    }
    return arr;
}

var arr1 = [4, 'Ulysses', 42, false];
console.log(double(arr1)); //: [4, 4, "Ulysses", "Ulysses", 42, 42, false, false]

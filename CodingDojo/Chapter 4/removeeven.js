/*
Remove Even-Length Strings

Build a standalone function to remove strings of even lengths
from a given array.
*/

function removeEven(arr) {
    for (var idx = arr.length-1; idx > 0; idx--) {
        if (arr[idx].length%2 == 0) {
            for (var i = idx; i < arr.length-1; i++) {
                var temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
            arr.pop();
        }
    }
    return arr;
}

var arr1 = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."];
console.log(removeEven(arr1));

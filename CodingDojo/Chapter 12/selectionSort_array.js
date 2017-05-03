/*
Array: Selection Sort

For review, create a function that uses
SelectionSort to sort an unsorted array in-place.

This sorting algorithm is an in-place comparison-based
algorithm in which the list is divided into two parts,
the sorted part at the left end and the unsorted part
at the right end. Initially, the sorted part is empty
and the unsorted part is the entire list.
*/

function selectSort(arr) {
    for (var runner1 = 0; runner1 < arr.length-1; runner1++) {
        // console.log(arr);
        var minIdx = runner1;
        for (var runner2 = runner1 + 1; runner2 < arr.length; runner2++) {
            if (arr[runner2] < arr[minIdx]) {
                minIdx = runner2;
            }
        }
        var temp = arr[runner1];
        arr[runner1] = arr[minIdx];
        arr[minIdx] = temp;
    }
    return arr;
}

var arr1 = [14, 33, 27, 10, 35, 19, 42, 44];
console.log(selectSort(arr1));

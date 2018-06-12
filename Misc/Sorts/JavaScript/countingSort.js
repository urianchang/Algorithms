/*
Counting Sort

Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values
(kind of hashing). Then doing some arithmetic to calculate the position of
each object in the output sequence.
*/

function countingSort(arr) {
    var countArr = [];
    //: Count each element in the given array, and put count at appropriate index
    for (var idx = 0; idx < arr.length; idx++) {
        if (countArr[arr[idx]] > 0) {
            countArr[arr[idx]] += 1;
        } else {
            countArr[arr[idx]] = 1;
        }
    }
    //: Modify count array by adding up previous counts
    for (var idx = 1; idx < countArr.length; idx++) {
        if (countArr[idx] === undefined) {
            countArr[idx] = 0;
        }
        if (countArr[idx - 1] === undefined) {
            countArr[idx - 1] = 0;
        }
        countArr[idx] = countArr[idx] + countArr[idx - 1];
    }
    //: Iterate through given array and check against count array to see where it goes
    var sortedArr = [];
    for (var idx = arr.length - 1; idx >= 0; idx--) {
        countArr[arr[idx]]--;
        sortedArr[countArr[arr[idx]]] = arr[idx];
    }
    //: Return sorted array
    return sortedArr;
}

var arr1 = [1, 4, 1, 2, 7, 5, 2];
console.log(`Before sorting: \n ${arr1} \n`)
arr1 = countingSort(arr1);
console.log(`After sorting: \n ${arr1}`)

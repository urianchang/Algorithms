/*
Array: Remove Duplicates

Given a sorted array, remove duplicate values. Because array elements are in order,
all duplicate values will be grouped together.
*/

function removeDups(arr) {
    var idx = 0;
    var count = 1;
    while (count < arr.length) {
        if (arr[idx] == arr[count]){
            count++;
        } else {
            arr[idx+1] = arr[count];
            idx++;
            count++;
        }
    }
    for (var x = 0; x < idx; x++) {
        arr.pop();
    }
    return arr;
}

var arr1 = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6];
console.log(removeDups(arr1));

/*
Array: Insertion Sort

Create a function to sort an unsorted array in-place.

Details -
An element which is to be 'insert'ed in this sorted
sub-list, has to find its appropriate place and then
it has to be inserted there.
*/

function insertSort(arr) {
    for (var i = 1; i < arr.length; i++) {
        if (arr[i-1] > arr[i]) {
            var temp = arr[i];
            for (var j = i; j > 0; j--) {
                arr[j] = arr[j-1];
                if (arr[i] >= arr[j-1]) {
                    arr[j-1] = temp;
                }
                if ((j-1) === 0) {
                    arr[0] = temp;
                }
            }
        }
    }
    return arr;
}

var arr1 = [3, 2, 4, 5, 1];
console.log(insertSort(arr1));

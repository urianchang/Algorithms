/*
Array: Bubble Sort

For review, create a function that uses BubbleSort to sort
an unsorted array in-place.
*/

function bubbleSort(arr) {
    var messy = true;
    while (messy) {
        messy = false;
        for (var i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i-1]) {
                messy = true;
                var temp = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = temp;
            }
        }
    }
    return arr;
}

var arr1 = [2, 6, 3, 1, 4, 5, 8, 7];
console.log(bubbleSort(arr1));

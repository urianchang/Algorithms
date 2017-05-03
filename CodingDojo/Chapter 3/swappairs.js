/*
Array: Swap Pairs

Swap positions of successive pairs of values of given array. If length is odd,
do not change the final element. For [1, 2, 3, 4], return [2, 1, 4, 3].
*/

function swap(arr) {
    if (arr.length%2 == 0) {
        for (var x = 0; x < arr.length; x+=2) {
            var temp = arr[x];
            arr[x] = arr[x+1];
            arr[x+1] = temp;
        }
    } else {
        for (var x = 0; x < arr.length-1; x+=2) {
            var temp = arr[x];
            arr[x] = arr[x+1];
            arr[x+1] = temp;
        }
    }
    return arr;
}

var arr1 = [1, 2, 3, 4];
var arr2 = [1, 2, 3, 4, 5];
console.log(swap(arr1));
console.log(swap(arr2));

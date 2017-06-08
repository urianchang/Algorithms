/*
Array Average (Warmup)

Always run through some quick algorithm problems
before any coding interview, to get yourself
warmed up. How about this one: return the average
value of an array of unsorted numbers.
*/

function avg(arr) {
    if (arr.length > 0) {
        sum = arr[0];
        for (var i = 1; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum/arr.length;
    } else {
        return "Array is empty";
    }
}

var arr1 = [1, 2, 3, 4, 5];
console.log(avg(arr1));
var arr2 = [];
console.log(avg(arr2));
arr2.push(1);
console.log(avg(arr2));

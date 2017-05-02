/*
Recursive "Tribonacci":

Write function rTrib(num) to mimic Fibonacci, adding
previous three values instead of two.

First three Tribonacci numbers are: 0, 0, 1.

Handle negatives and non-integers appropriately
and inexpensively.
*/

function rTrib(num) {
    //: To handle non-integer, round down to integer
    var int = Math.floor(num)
    //: Break cases
    if (int <= 1) {
        return 0;
    }
    if (int == 2) {
        return 1;
    }
    return rTrib(int - 1) + rTrib(int - 2) + rTrib(int - 3);
}

console.log(rTrib(3));  // 1
console.log(rTrib(4));  // 2
console.log(rTrib(5));  // 4
console.log(rTrib(6));  // 7
console.log(rTrib(4.65));   // 2

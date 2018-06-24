//: https://www.hackerrank.com/challenges/js10-bitwise/problem

/*
Additional Reading:
  * https://www.hackerrank.com/challenges/js10-bitwise/topics/javascript-bitwise-operators
  * https://www.hackerrank.com/topics/bit-manipulation
*/

function getMaxLessThanK(n, k) {
    if ((k | k-1) > n) {
        return (k-2);
    }
    return (k-1);
}

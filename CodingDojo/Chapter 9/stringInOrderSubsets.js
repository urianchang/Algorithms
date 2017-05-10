/*
String: In-Order Subsets

Create strSubsets(str). Return an array with every possible
in-order character subset of str. The resultant array itself
need not be in any specific order -- it is the subset of letters
in each string that must be in the same order as they were in the
original string.
*/

function strSubsets(str) {
    return makeSubsets(str, [], str.length - 1);
}

function makeSubsets(str, arr, memo) {
    if (memo == str.length - 1) {
        arr.push("");
    }
    if (memo < 0) {
        arr.push(str);
        return arr;
    }
    var char = str[memo];
    arr.push(char);
    for (var i = 0; i < memo; i++) {
        arr.push(str[i] + char);
    }
    return makeSubsets(str, arr, memo - 1);
}

var str1 = "abc";
console.log(strSubsets(str1));   // ["", "c", "b", "bc", "a", "ac", "ab", "abc"] in any order

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
        // arr.push(str);
        return arr;
    }
    var char = str[memo];
    arr.push(char);
    for (var i = 0; i < memo; i++) {
        for (var idx = i+1; idx < str.length; idx++){
            // console.log(i, idx, str.slice(i, idx));
            if (idx == i) {
                continue;
            } else if (idx <= memo) {
                arr.push(str.slice(i, idx) + char);
            } else {
                var newSub = str.slice(i, memo-1) + char + str.slice(idx);
                if (arr.includes(newSub) === false) {
                    arr.push(newSub);
                }
            }
        }
    }
    return makeSubsets(str, arr, memo - 1);
}

var str1 = "abc";
console.log(strSubsets(str1));   // ["", "c", "b", "bc", "a", "ac", "ab", "abc"] in any order

var str2 = "abcd";
console.log(strSubsets(str2));

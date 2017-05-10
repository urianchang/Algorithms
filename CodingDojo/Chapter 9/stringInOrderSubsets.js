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

//: Helper function that uses recursion and memoization to make array of subsets
function makeSubsets(str, arr, memo) {
    //: Include an empty string subset
    if (memo == str.length - 1) {
        arr.push("");
    }
    //: Break case - When memo (index) is less than zero
    if (memo < 0) {
        return arr;
    }
    //: Get the specific character at memo (index)
    var char = str[memo];
    arr.push(char);

    //: Using two for-loops to generate string subsets since string slice is used
        //: First for-loop determines starting point of string slice
    for (var i = 0; i < memo; i++) {
        //: Second for-loop determines ending point of string slice
        for (var idx = i+1; idx < str.length; idx++) {
            //: If starting and ending slice indices are the same, continue
            if (idx == i) {
                continue;
            //: If ending slice index is less than memo, add the substring to array
            } else if (idx <= memo) {
                arr.push(str.slice(i, idx) + char);
            } else {
                //: If ending slice index is greater than memo...
                var newSub = str.slice(i, memo-1) + char + str.slice(idx);
                //: Check for duplicates...
                if (arr.includes(newSub) === false) {
                    arr.push(newSub);
                }
            }
        }
    }
    //: Recurisve call - Return function with memo reduced by 1
    return makeSubsets(str, arr, memo - 1);
}

var str1 = "abc";
console.log(strSubsets(str1));   // ["", "c", "b", "bc", "a", "ac", "ab", "abc"] in any order

var str2 = "abcd";
console.log(strSubsets(str2).length);

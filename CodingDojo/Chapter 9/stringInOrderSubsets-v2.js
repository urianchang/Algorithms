/*
String: In-Order Subsets

Create strSubsets(str). Return an array with every possible
in-order character subset of str. The resultant array itself
need not be in any specific order -- it is the subset of letters
in each string that must be in the same order as they were in the
original string.

Version 2 - Works for word of any length.

*/

//: Main function
function makeSubset(string) {
    var array = subs(string, [], 0);
    array.push(string);
    return array;
}
//: Subset helper function
function subs(string, array, memo) {
    // console.log(string, array, memo);
    if (memo === string.length) {
        return array;
    }
    for (var i = 0; i < string.length; i++) {
        // console.log("memo:", memo, "string:", string);
        if (i < memo) { continue; }
        var temp = string.split('');
        //: Take out char at index.
        temp.splice(i, 1).join('');
        var b = temp.join('');
        // console.log("b:", b);
        array.push(b);
        array = array.concat(subs(b, [], i));
    }
    return array;
}

var str = "abc";
// console.log(subs("abcd", [], 0));
console.log(makeSubset(str));


//: For research...
// abcd = 2 + 4 + 6 + 4 = 16
// first: 1
// second: 4
// third: 6
// fourth: 4
// fifth: 1
// a -> bcd
//     b -> cd
//     c -> bd
//     d -> bc
// b -> acd
//     a -> cd !
//     c -> ad
//     d -> ac
// c -> abd
//     a -> bd !
//     b -> ad !
//     d -> ab
// d -> abc
//     a -> bc !
//     b -> ac !
//     c -> ab !

// var arr1 = [1, 2, 3];
// var arr2 = [4, 5, 6];
// console.log(arr1.concat(arr2));
// console.log(arr1);

// var strArr = str.split('')
// console.log(strArr.splice(2, 1).join(''));
// console.log(strArr.join(''));

// abc = 8
// first level: abc + '' = 1
// second level: ab, ac, bc = 3
// third level: a, b, c = 3
// fourth level: '' = 1
// a -> bc
//      memo = 1
//     b -> c
//     c -> b
// b -> ac
//      memo = 1
//     a -> c !
//     c -> a
// c -> ab
//      memo = 1
//     a -> b !
//     c -> a !

//     1
//    1 1
//   1 2 1
//  1 3 3 1
// 1 4 6 4 1

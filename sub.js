var str = "abcd";

// abcd + '' = 2 + 4 + 6 + 4 = 16
// 3 + 1
// 3 + 2 + 1
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


function subs(string, array, memo) {
    // if (memo === Math.ceil(string.length/2)) {
    //     return array;
    // }
    if (memo === 3) {
        // console.log(string);
        return array;
    }
    for (var i = 0; i < string.length; i++) {
        console.log(memo);
        // if (i > memo) { break; }
        var temp = string.split('');
        //: Take out char at index. Memo dictates which iteration?
        var a = temp.splice(i, memo).join('');
        var b = temp.join('');
        // console.log("a:", i, memo, a);
        // console.log("b:", b);
        // array.push(a);
        array.push(b);
        array = array.concat(subs(b, [], memo+1));
        // array = array.concat(a);
        // array = array.concat(subs(b, [], memo));
        // array.push(subs(b, array, 1));
        // array.push(temp.splice(i, memo).join(''));
        // array.push(temp.join(''));
    }
    return subs(string, array, memo+1);
    // return "Done";
}

console.log(subs("abc", [], 0)); //: Fuck.

//: Arnold's helper function
function subsetBuilder(str,subsetLength,arr){
    if(subsetLength === 1){return [str[0]]}
    if(subsetLength === str.length && arr === undefined){return [str]}
    if(arr === undefined){
        arr = [];
        for(var i = 0; i < str.length - subsetLength + 1; i++){
            arr.push(str[0]);
        }
        return subsetBuilder(str.slice(1),subsetLength,arr)
    }
    for(var i = 0; i < arr.length; i++){
        arr[i] += str[i];
    }
    if(arr[0].length === subsetLength){
        return arr
    }
    return subsetBuilder(str.slice(1),subsetLength,arr)
}

// console.log(subsetBuilder("abcde",1));
// console.log(subsetBuilder("abcde",3));
// console.log(subsetBuilder("abcde",5));

function main(str) {
    var newArr = [];
    for (var i = 0; i < str.length; i++) {
        var temp = str.slice(i);
        // console.log(temp);
        for (var idx = 1; idx <= temp.length; idx++) {
            newArr = newArr.concat(subsetBuilder(temp, idx));
        }
    }
    return newArr;
}

// console.log(main("abcd")); //: Missing 'abd' and ''

/*
String: Is Palindrome

Create a function that returns a Boolean whether the string is a strict
palindrome. Do not ignore spaces, punctuation, and capitalization.

Second: now do ignore white space, capitalization and punctuation.
    -- The problem probably wants to use Switch cases, but I'm lazy, so I'm going to use RegEx instead. (Thanks Google!)
*/

function palindrome1(string) {
    for (var i = 0; i < string.length/2; i++) {
        if (string[i] != string[string.length-1-i]){
            return false;
        }
    }
    return true;
}

function palindrome2(string) {
    var lowerStrArr = string.toLowerCase().match(/[a-z]/g);
    for (var i = 0; i < lowerStrArr.length/2; i++) {
        if (lowerStrArr[i] != lowerStrArr[lowerStrArr.length-1-i]){
            return false;
        }
    }
    return true;
}

var str1 = "racecar";
var str2 = " a x a";
var str3 = "asdf";
var str4 = "Dud";
// console.log(palindrome1(str1));
// console.log(palindrome1(str2));
// console.log(palindrome1(str3));
// console.log(palindrome1(str4));
console.log(palindrome2(str1));
console.log(palindrome2(str2));
console.log(palindrome2(str3));
console.log(palindrome2(str4));

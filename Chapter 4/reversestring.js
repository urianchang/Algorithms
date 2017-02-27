/*
String: Reverse

Implement reverseString(str) that, given string, returns that string with
characters reversed.
*/

function reverseString(str) {
    var newStr = "";
    for (var idx = str.length-1; idx >= 0; idx--) {
        newStr += str[idx];
    }
    return newStr;
}

var str1 = "creature";
console.log(reverseString(str1));

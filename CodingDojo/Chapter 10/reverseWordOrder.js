/*
Reverse Word Order:

Create a function that, given a string of
words (with spaces), returns new string
with words in reverse sequence.
*/

function reverseWordOrder(str) {
    var wordArr = str.split(" ");
    for (var i = 0; i < wordArr.length/2; i++) {
        var temp = wordArr[i];
        wordArr[i] = wordArr[wordArr.length - 1 - i];
        wordArr[wordArr.length - 1 - i] = temp;
    }
    return wordArr.join(" ");
}

var str1 = "This is a test";
console.log(reverseWordOrder(str1));
var str2 = "This is not a test for you";
console.log(reverseWordOrder(str2));

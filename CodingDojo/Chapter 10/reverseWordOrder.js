/*
Reverse Word Order:

Create a function that, given a string of
words (with spaces), returns new string
with words in reverse sequence.

BONUS: handle punctuation and capitalization.
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

// var str1 = "This is a test";
// console.log(reverseWordOrder(str1));
// var str2 = "This is not a test for you";
// console.log(reverseWordOrder(str2));

var str1 = "Hello world, i am here; right?";

//: For the bonus...
function revWordOrder(str) {
    var newArr = [];
    var endingPunctuation = "";
    //: Split string into words
    var wordArr = str.split(" ");
    //: Iterate through array backwards
    for (var i = wordArr.length - 1; i >= 0; i--) {
        var word = "";
        //: Split every word into characters
        var charArr = wordArr[i].split("");
        //: Iterate through characters
        for (var idx = 0; idx < charArr.length; idx++) {
            if (i === wordArr.length - 1 && idx === 0) {
                charArr[idx] = charArr[idx].toUpperCase();
            }
            if (i === 0 && idx === 0) {
                charArr[idx] = charArr[idx].toLowerCase();
            }
            if (charArr[idx] === "," || charArr[idx] === ";" || charArr[idx] === "'" || charArr[idx] === ":" || charArr[idx] === '"') {
                newArr[(wordArr.length - 1) - (i + 1)] = newArr[(wordArr.length - 1) - (i + 1)] + charArr[idx];
                continue;
            }
            if (charArr[idx] === "." || charArr[idx] === "!" || charArr[idx] === "?") {
                endingPunctuation = charArr[idx];
                continue;
            }
            word += charArr[idx];
        }
        newArr.push(word);
    }
    newArr[newArr.length - 1] = newArr[newArr.length - 1] + endingPunctuation;
    return newArr.join(" ");
}
console.log(revWordOrder(str1));

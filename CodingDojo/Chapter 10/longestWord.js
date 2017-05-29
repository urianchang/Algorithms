/*
Longest Word:

Create a function that, given a string of words,
returns the longest word.

Bonus: handle punctuation
*/

function findLongestWord(str) {
    var wordArr = str.split(" ");
    var longestWord = wordArr[0];
    for (var i = 1; i < wordArr.length; i++) {
        if (wordArr[i].length > longestWord.length) {
            longestWord = wordArr[i];
        }
    }
    return longestWord;
}

var str1 = "Snap crackle pop makes the world go round!";
console.log(findLongestWord(str1));

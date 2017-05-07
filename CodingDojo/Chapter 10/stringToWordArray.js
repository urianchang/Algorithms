/*
String to Word Array

Given a string of words (with spaces,
tabs, and linefeeds), return an array
of words.

Bonus: handle punctuation
*/

function wordArr(str) {
    var arr = [];
    var wordStr = "";
    for (var i=0; i < str.length; i++) {
        if (str[i] == " " || str[i] == "\t" || str[i] == "\n") {
            arr.push(wordStr);
            wordStr = "";
        } else if (str[i] == "." || str[i] == "!" || str[i] == "?" || str[i] == "," || str[i] == "'" || str[i] == '"' || str[i] == ":" || str[i] == ";") {
            continue;
        } else {
            wordStr += str[i];
        }
    }
    arr.push(wordStr);
    return arr;
}

var str1 = "Life is not a drill!";
console.log(wordArr(str1));

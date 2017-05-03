/*
Acronyms

Create a function that, given a string, returns the string's acronym
(first letters only, capitalized).
*/

function acronyms(str) {
    var strArr = str.split(" ");
    var retStr = "";
    for (var ind = 0; ind < strArr.length; ind++) {
        if (strArr[ind] == false) {
            continue;
        } else {
            retStr += strArr[ind][0].toUpperCase();
        }
    }
    return retStr;
}

var str1 = " there's no free lunch - gotta pay yer way.";
console.log(acronyms(str1));
var str2 = "Live from New York, it's Saturday Night!";
console.log(acronyms(str2));

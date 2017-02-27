/*
String: Get Digits

Create a JavaScript function that given a string, returns
the integer made from the string's digits.
*/

function getDigits(str) {
    var stringArr = str.split("");
    var intStr = "";
    for (var ind = 0; ind < stringArr.length; ind++) {
        if (stringArr[ind]%1 == 0) {
            intStr += stringArr[ind];
        }
    }
    return intStr/1;
}

var str1 = "0s1a3y5w7h9a2t4?6!8?0";
console.log(getDigits(str1));

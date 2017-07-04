/*
Drop the Mike

Create a standalone function that accepts
an input string, removes leading and trailing
white space, capitalizes the first letter of
every word, and returns that string. If original
string contains the word "Mike" anywhere, immediately
return "stunned silence" instead.
*/

function drop(str) {
    const strArr = str.split(" ");
    let newStr = [];
    for (var i = 0; i < strArr.length; i++) {
        if (strArr[i] === "Mike") {
            return "stunned silence";
        }
        newStr.push(strArr[i][0].toUpperCase() + strArr[i].substring(1));
    }
    return newStr.join(' ');
}

var str1 = "hello world, my name is urian";
var str2 = "what's up, Mike";
console.log(drop(str1));    //: Hello World, My Name Is Urian
console.log(drop(str2));    //: stunned silence

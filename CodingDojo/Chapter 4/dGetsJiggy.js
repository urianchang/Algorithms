/*
D Gets Jiggy

Write a function that accepts as a parameter a string containing
someone's name. Return a string containing the following oh-so-cool
greeting: strip off the first letter of the name, capitalize this new word,
and add " to the [first letter]!"
*/

function jiggy(str) {
    var wordArr = str.split("");
    var firstLetter = wordArr[0];
    for (var i = 1; i < wordArr.length; i++) {
        var temp = wordArr[i];
        wordArr[i] = wordArr[i-1];
        wordArr[i-1] = temp;
    }
    wordArr.pop();
    wordArr = wordArr.join("");
    return wordArr.charAt(0).toUpperCase() + wordArr.slice(1) + " to the " + firstLetter + "!";
}

var str1 = "Dylan";
console.log(jiggy(str1));

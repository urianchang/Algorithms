/*
Remove Blanks

Create a function that given a string, returns all of the string's
contents, but without blanks.
*/

function removeBlanks(str) {
    return str.split(" ").join("");
}

var str1 = "hello world my name is urian";
console.log(removeBlanks(str1));
var str2 = " Pl ayTha tF u nkyM usi       c   ";
console.log(removeBlanks(str2));

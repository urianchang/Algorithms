/*
Parens Valid:

Create a function that, given an input string str, returns a Boolean whether
parentheses in str are valid. Valid sets of parentheses always open before they
close.
*/

function parensValid(str){
    var counto = 0;
    var countc = 0;
    for (var i = 0; i < str.length; i++) {
        if (countc > counto){
            return false;
        }
        if (str[i] == "(") {
            counto++;
        }
        if (str[i] == ")") {
            countc++;
        }
    }
    if (countc == counto) {
        return true;
    }
    return false;
}

var string1 = "Y(3(p)p(3)r)s";
var string2 = "N(0(p)3";
var string3 = "N(0)t )0(k";
var string4 = ")()(()";
console.log(parensValid(string1));
console.log(parensValid(string2));
console.log(parensValid(string3));
console.log(parensValid(string4));

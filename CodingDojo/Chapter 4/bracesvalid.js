/*
Braces Valid

Given a sequence of parentheses, braces, and brackets, determine whether it is valid.
*/

function bracesValid(str) {
    // var countp = 0;
    // var countb = 0;
    // var countc = 0;
    var count = 0;
    var last = [];
    for (var i = 0; i < str.length; i++) {
        if (count == -1) {
            return false;
        }
        if (str[i] == "{" || str[i] == "[" || str[i] == "("){
            count++;
            last.push(str[i]);
        }
        if (str[i] == "]") {
            if (last[last.length-1] == "[") {
                count--;
                last.pop();
            } else {
                return false;
            }
        }
        if (str[i] == ")") {
            if (last[last.length-1] == "(") {
                count--;
                last.pop()
            } else {
                return false;
            }
        }
        if (str[i] == "}") {
            if (last[last.length-1] == "{") {
                count--;
                last.pop()
            } else {
                return false;
            }
        }
    }
    if (count == 0) {
        return true;
    }
    return false;
}

var string1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
var string2 = "D(i{a}l[ t]o)n{e";
var string3 = "A(l)s[O(n]O{t) O}k";
console.log(bracesValid(string1));
console.log(bracesValid(string2));
console.log(bracesValid(string3));

//: https://www.hackerrank.com/challenges/js10-regexp-1/problem
//: https://www.hackerrank.com/challenges/js10-regexp-1/topics/javascript-regex

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
     //: \1 matches first captured character
    const re = /^([a, e, i, o, u]).*\1$/;
    //: Or use RegExp
    // const re = new RegExp(/^([a, e, i, o, u]).*\1$/);

    /*
     * Do not remove the return statement
     */
    return re;
}

//: https://www.hackerrank.com/challenges/js10-regexp-3/problem

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match ALL occurrences of numbers in a string.
     */
     //: Use 'g' (global) flag to match all occurrences
     const re = /\d+/g;

    /*
     * Do not remove the return statement
     */
    return re;
}

const re = regexVar();
const s = "102, 1948948 and 1.3 and 4.5";
const r = s.match(re);

for (const e of r) {
  console.log(e);
}

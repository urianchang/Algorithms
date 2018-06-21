//: https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem
/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    let rev = s;
    try {
      let arr = s.split("");
      rev = arr.reverse().join("");
    } catch (err) {
      console.log(err.message);
    } finally {
      console.log(rev);
    }
}

reverseString("hello");
reverseString(123);

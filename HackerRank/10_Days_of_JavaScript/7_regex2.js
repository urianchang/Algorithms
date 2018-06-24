//: https://www.hackerrank.com/challenges/js10-regexp-2/problem
function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.',
     * followed by one or more letters (A-Z, a-z).
     */
     const re = /^(Mr|Mrs|Ms|Dr|Er)\.([A-Za-z])+$/;

    /*
     * Do not remove the return statement
     */
    return re;
}

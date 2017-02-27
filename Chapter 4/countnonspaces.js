/*
Count Non-Spaces

Accept a string and return the number of non-space characters
found in the string.
*/

function countNS(str) {
    var strArr = str.split("");
    var count = 0;
    for (var ind = 0; ind < strArr.length; ind++) {
        if (strArr[ind] == false) {
            continue;
        } else {
            count++;
        }
    }
    return count;
}

var str1 = "Honey pie, you are driving me crazy";
// Expected output is 29.
console.log(countNS(str1));
